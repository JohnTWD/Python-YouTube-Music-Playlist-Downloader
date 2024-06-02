import os;
from traceback import format_exc;
from time import sleep;

from constants import getBaseUrl, setBaseUrl;
from utils.miscUtils import *;
from utils.playlistParserUtils import *;
from utils.downloaderUtils import AudioInfo, getBestAudio, downloadAudio;
from utils.orderingUtils import *;
from classes.PlaylistVideo import PlaylistVideo;
from classes.AudioInfo import AudioInfo;
from classes.Playlist import Playlist;

def doDownloadAudioFile(playlistVideo: PlaylistVideo) -> None:
	if (handleExistingDownloads(playlistVideo)):
		bestAudio: AudioInfo = getBestAudio(playlistVideo);
		downloadAudio(bestAudio);


def main():
	goHome();
	print('@' + os.getcwd());
	
	customInstance: str = input(f"If the main instance `{getBaseUrl()}` is down, you can choose a custom piped api instance here.\nElse, leave this empty: ");
	if (customInstance): # custom instance is not empty
		setBaseUrl(customInstance);
	
	print(f"baseUrl={getBaseUrl()}");
	
	plId: str = input("Enter playlist ID: ");
	plInfo: Playlist = getPlaylist(plId);
	
	print("\n\n\n\nPlaylist fetched.");
	print(f"Playlist name: {plInfo.name}");
	print(f"Uploader: {plInfo.uploader}");
	
	if (input("View playlist items? (y)") == 'y'):
		plInfo.show();

	isValidSelection:  bool = False;
	shouldDownloadAll: bool = False;
	selectedRange: str;
	while (not isValidSelection):
		plSize: int = len(plInfo.videos);

		print("Choose which parts of the playlist to download\nE.g. \"2-6, 9, 12-16\" and this may not be necessarilly ordered");
		selectedRange = input(f"Range: 1-{plSize}\nOr, you can leave this blank to download the entire thing: ");

		if (selectedRange == ''):
			shouldDownloadAll = True;
			isValidSelection = True;
		else:
			isValidSelection = isGoodRange(plSize, selectedRange);
	dlIndex: set = getSelectedIndices(selectedRange);

	
	# create output folder and enter it
	makeFolderEnter("OUTPUT");
	print('@' + os.getcwd());

	if (input("Begin download? (y)") != 'y'):
		return;
	
	for video in plInfo.videos:
		assert isinstance(video, PlaylistVideo);

		if (shouldDownloadAll or (video.index in dlIndex)):
			try:
				doDownloadAudioFile(video);
			except Exception:
				try:
					print(f"Shit failed! Retrying download {video.title} from {video.link}; ", end="", flush=True);
					sleep(5);
					doDownloadAudioFile(video);
				except Exception:
					print(f"Failed to download due to the following error:\n{format_exc()}\nGiving up and skipping...", flush=True);
if (__name__=="__main__"):	main();