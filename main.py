import requests;
import os;
from subprocess import call;

from constants import baseUrl;
from constants import setBaseUrl;
from utils.miscUtils import *;
from utils.playlistParserUtils import *;
from utils.downloaderUtils import getBestAudio;
from utils.downloaderUtils import downloadAudio;

def doDownloadAudioFile(idVideo: str) -> None:
  bestAudio: AudioInfo = getBestAudio(idVideo);
  downloadAudio(bestAudio);


def main():
  goHome();
  print('@' + os.getcwd());

  customInstance: str = input("If the main instance `https://pipedapi.kavin.rocks` is down, you can choose a custom piped api instance here.\nElse, leave this empty: ");
  if (not not customInstance): # custom instance is not empty
    setBaseUrl(customInstance);

  print(f"baseUrl={baseUrl}");

  plId: str = input("Enter playlist ID: ");
  plInfo: Playlist = getPlaylist(plId);

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
    try:
      doDownloadAudioFile(video);
    except Exception:
      try:
        print(f"Shit failed! Retrying downloading {video.title} from {video.link}; ", end="");
        doDownloadAudioFile(video.link);
      except Exception:
        print("Failed to download. Giving up and skipping...");

  
if (__name__=="__main__"):  main();