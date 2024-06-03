import os
from urllib.parse import quote;
import requests

from constants import getBaseUrl, getTimeStamp, homeDir;
from utils.miscUtils import removeIllegalChar, logF;
from classes.Playlist import Playlist;
from classes.PlaylistVideo import PlaylistVideo;

def __writeVideoToCache(plVid: PlaylistVideo) -> None:
	out: str =  f"{plVid.index} {plVid.link} {plVid.title}"
	logF(out, fileName="videoscache", console=False);


# Playlist parser
def getPlaylist(playlistId: str) -> PlaylistVideo:
	playlistUrl: str = f"{getBaseUrl()}/playlists/{playlistId}";
	#videos: list = [];

	# Fetch initial playlist data
	response: requests.Response = requests.get(playlistUrl);
	if (response.status_code != 200):
		raise Exception("Can't fetch playlist");

	data: dict = response.json();

	plName:     str = data.get("name", "Unknown Playlist");
	plUploader: str = data.get("uploader", "Unknown Uploader");

	if (not os.path.exists(os.path.join(homeDir, "logs", getTimeStamp(), "videoscache.txt"))): # playlist no exist yet, prepend the playlist data at the top
		logF(f"{playlistId}\n{plName}\n{plUploader}\n---BEGIN PLAYLIST DATA (*DO NOT* EDIT THIS LINE)---", fileName="videoscache", console=False);

	i: int = 1;  # make idx start from 1 because thats how most people know shit

	for raw in data["relatedStreams"]:
		assert isinstance(raw, dict);
		__writeVideoToCache(
			PlaylistVideo(
				i, removeIllegalChar(raw["title"]), raw["url"][9:]
			)
		);
		i += 1;

	# Deal with the pagesss
	while ("nextpage" in data and data["nextpage"]):
		nextpage: str = quote(data["nextpage"]);
		nextUrl:  str = f"{getBaseUrl()}/nextpage/playlists/{playlistId}?nextpage={nextpage}";
		
		logF(nextUrl)

		response = requests.get(nextUrl);
		if (response.status_code != 200):
			raise Exception("Can't get next playlist page");

		data: dict = response.json();

		for raw in data["relatedStreams"]:
			assert isinstance(raw, dict);
			__writeVideoToCache(
				PlaylistVideo(
					i, removeIllegalChar(raw["title"]), raw["url"][9:]
				)
			);
			i += 1;

	return Playlist(
		plName,
		plUploader,
		os.path.join(homeDir, "logs", getTimeStamp(), "videoscache.txt")
	);