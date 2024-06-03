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

def errlog(problemObj: PlaylistVideo, reason: str, plId: str) -> None:
	if (not os.path.exists(os.path.join(homeDir, "logs", getTimeStamp(), "FAILLOGS.txt"))): # error file does not exist yet
		logF(f"ERROR LOG OF PLAYLIST: {plId}", console=False, fileName="FAILLOGS"); # this is so we create a new file with playlist ID as header at the top

	logF(
		f"{problemObj.index}:    {problemObj.title}    {reason}    @https://www.youtube.com/watch?v={problemObj.link}", 
		fileName = "FAILLOGS",
		console = False, 
	);

def init() -> None:
	setTimeStamp();
	goHome();

	makeFolder("logs", shutUp=True);
	makeFolder(os.path.join("logs", getTimeStamp()));


def main():
	while (True):
		init();

		logF('@' + os.getcwd());

		logF(f"Current time: {getTimeStamp()}");

		customInstance: str = input(f"If the main instance `{getBaseUrl()}` is down, you can choose a custom piped api instance here.\nElse, leave this empty: ");
		if (customInstance): # custom instance is not empty
			setBaseUrl(customInstance);

		logF(f"baseUrl={getBaseUrl()}");

		logF(
			"\nEnter playlist. You can choose to load a playlist from a cache or the ID of the playlist" +
			"\nPlaylist ID is at ...youtube.com/playlist?list=PLgyjA..." +
			"\nCopy it from the back part --------------------^^^^^^^^^" +
			"\nAlternatively, provide the cache file. Enter the WHOLE filepath of the cache file"
		);

		plId: str = input("Enter playlist ID: ");

		plInfo: Playlist = None;
		if (os.path.exists(plId)):	# assume its a cache
			plInfo = Playlist.loadCache(plId);
		else:
			plInfo = getPlaylist(plId); # else its probably a playlistId

		plDetails: list = Playlist.getDetails(plInfo.videoCache);

		logF(f"\n\n\n\nPlaylist ({plDetails[0]}) fetched.");
		logF(f"Playlist name: {plDetails[1]}");
		logF(f"Uploader: {plDetails[2]}");

		del plDetails;

		if (input("View playlist items? (y)") == 'y'):
			plInfo.show();

		isValidSelection:  bool = False;
		shouldDownloadAll: bool = False;
		selectedRange: str;
		while (not isValidSelection):
			plSize: int = plInfo.getCount();

			logF(f"Choose which parts of the playlist to download\nE.g. \"2-6, 9, 12-16\". Ordering is optional\nRange: 1-{plSize}");
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

		for video in plInfo.eachInCache():
			assert isinstance(video, PlaylistVideo);

			if (shouldDownloadAll or (video.index in dlIndex)):
				try:
					doDownloadAudioFile(video);
				except Exception:
					try:
						logF(f"Shit failed! Retrying download {video.title} from {video.link}; ", end="", flush=True);
						sleep(5);
						doDownloadAudioFile(video);
					except Exception as e:
						logF(f"Failed to download due to the following error:\n{format_exc()}\nGiving up and skipping...", flush=True);
						errlog(video, e, plId);

		logF("\n\nALL DOWNLOADS DONE. READY FOR NEW BATCH\n");
if (__name__=="__main__"):	main();