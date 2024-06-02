from dataclasses import dataclass;
from urllib.parse import quote;
import requests;

from constants import getBaseUrl;

@dataclass
class PlaylistVideo:
	index: int;
	title: str;
	link:  str;

@dataclass
class Playlist:
	name:     str;
	uploader: str;
	videos:   list; # PlaylistVideos

	def show(self) -> None:
		print("index    -   title   -   url");
		for video in self.videos:
			print(f"{video.index}   {video.title}   {video.link}");
#    def addVideoEntry(self, newEntry: dict) -> None:
#        self.videos.update(newEntry);

# Playlist parser
def getPlaylist(playlistId: str) -> Playlist:
	playlistUrl: str = f"{getBaseUrl()}/playlists/{playlistId}";
	videos: list = [];

	# Fetch initial playlist data
	response: requests.Response = requests.get(playlistUrl);
	if (response.status_code != 200):
		raise Exception("Can't fetch playlist");

	data: dict = response.json();
	videos.extend(data["relatedStreams"]);
	
	plName:     str = data.get("name", "Unknown Playlist");
	plUploader: str = data.get("uploader", "Unknown Uploader");

	# Deal with the pagesss
	while ("nextpage" in data and data["nextpage"]):
		nextpage: str = quote(data["nextpage"]);
		nextUrl:  str = f"{getBaseUrl()}/nextpage/playlists/{playlistId}?nextpage={nextpage}";
		
		print(nextUrl)

		response = requests.get(nextUrl);
		if (response.status_code != 200):
			raise Exception("Can't get next playlist page");

		data: dict = response.json();
		videos.extend(data["relatedStreams"]);

	allVideos: list = []; # list of PlaylistVideo

	i: int = 1;  # make idx start from 1 because thats how most people know shit
	for video in videos:
		allVideos.append(
			PlaylistVideo(
				i, 
				video["title"], 
				video["url"][9:]
			)
		);

		i += 1;
	
	return Playlist(
		plName,
		plUploader,
		allVideos
	);