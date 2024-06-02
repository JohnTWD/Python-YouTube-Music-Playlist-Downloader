import os;
from traceback import format_exc;
from time import sleep;

from constants import getBaseUrl, setBaseUrl;
from utils.miscUtils import *;
from utils.playlistParserUtils import *;
from utils.downloaderUtils import AudioInfo, getBestAudio, downloadAudio;

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
	
	if (input("View playlist items? (Y)") == 'Y'):
		plInfo.show();
	
	# create output folder and enter it
	makeFolderEnter("OUTPUT");
	print('@' + os.getcwd());

	if (input("Begin download? (Y)") != 'Y'):
		return;
	
	for video in plInfo.videos:
		assert isinstance(video, PlaylistVideo);
		try:
			doDownloadAudioFile(video);
		except Exception:
			try:
				print(f"Shit failed! Retrying downloading {video.title} from {video.link}; ", end="", flush=True);
				sleep(5);
				doDownloadAudioFile(video.link);
			except Exception:
				print(f"Failed to download due to the following error:\n{format_exc()}\nGiving up and skipping...", flush=True);
if (__name__=="__main__"):	main();