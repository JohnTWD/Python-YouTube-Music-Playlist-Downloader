import os;
from traceback import format_exc;
from time import sleep;

from constants import getBaseUrl, setBaseUrl, getTimeStamp, setTimeStamp;
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
	while (True):
		goHome();
		makeFolder("logs");
		logF('@' + os.getcwd());

		setTimeStamp();
		logF(f"Current time: {getTimeStamp()}");

		customInstance: str = input(f"If the main instance `{getBaseUrl()}` is down, you can choose a custom piped api instance here.\nElse, leave this empty: ");
		if (customInstance): # custom instance is not empty
			setBaseUrl(customInstance);

		logF(f"baseUrl={getBaseUrl()}");

		plId: str = input("Enter playlist ID: ");
		plInfo: Playlist = getPlaylist(plId);

		logF(f"\n\n\n\nPlaylist ({plId}) fetched.");
		logF(f"Playlist name: {plInfo.name}");
		logF(f"Uploader: {plInfo.uploader}");

		if (input("View playlist items? (y)") == 'y'):
			plInfo.show();

		isValidSelection:  bool = False;
		shouldDownloadAll: bool = False;
		selectedRange: str;
		while (not isValidSelection):
			plSize: int = len(plInfo.videos);

			logF("Choose which parts of the playlist to download\nE.g. \"2-6, 9, 12-16\". Ordering is optional\nRange: 1-{plSize}");
			selectedRange = input(f"Or, you can leave this blank to download the entire thing: ");

			if (selectedRange == ''):
				shouldDownloadAll = True;
				isValidSelection = True;
			else:
				isValidSelection = isGoodRange(plSize, selectedRange);
		dlIndex: set = getSelectedIndices(selectedRange);


		# create output folder and enter it
		makeFolderEnter("OUTPUT");
		logF('@' + os.getcwd());

		if (input("Begin download? (y)") != 'y'):
			continue;

		for video in plInfo.videos:
			assert isinstance(video, PlaylistVideo);

			if (shouldDownloadAll or (video.index in dlIndex)):
				try:
					doDownloadAudioFile(video);
				except Exception:
					try:
						logF(f"Shit failed! Retrying download {video.title} from {video.link}; ", end="", flush=True);
						sleep(5);
						doDownloadAudioFile(video);
					except Exception:
						logF(f"Failed to download due to the following error:\n{format_exc()}\nGiving up and skipping...", flush=True);

		logF("\n\nALL DOWNLOADS DONE. READY FOR NEW BATCH\n");
if (__name__=="__main__"):	main();