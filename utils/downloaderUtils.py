import requests;
import os;
import argparse;
from subprocess import call;

from constants import getBaseUrl
from utils.miscUtils import removeIllegalChar, logF;
from classes.AudioInfo import AudioInfo;
from classes.PlaylistVideo import PlaylistVideo;


def __convertFile(audioInfo: AudioInfo) -> None:
	fileInPath:  str = os.path.join(os.getcwd(), audioInfo.title + ".temp");
	fileOutPath: str = os.path.join(os.getcwd(), audioInfo.title + ".mp3");
	
	# the actual conversion
	command: str = ["ffmpeg", "-loglevel", '0', "-i",  fileInPath, "-metadata", f"artist={audioInfo.artist}", fileOutPath];
	call(command);

	if (os.path.exists(fileOutPath)):
		os.remove(fileInPath);   # get rid of the original file
		logF(f'Converted: {fileOutPath} to MP3');
	else:
		raise Exception("Something went wrong with conversion. Leaving temp file alone...");


def downloadAudio(audioInfo: AudioInfo) -> None:
	logF("Beginning download...", end="", flush=True);
	filePath: str = os.path.join(os.getcwd(), audioInfo.title + ".temp");

	with requests.get(audioInfo.url, stream=True) as r:
		r.raise_for_status();

		with open(filePath, "wb") as f:
			i: int = 0;
			for chunk in r.iter_content(chunk_size=8192):
				if (i >= 50):
					logF('.', end='', flush=True);
					i = 0;
				f.write(chunk);
				i += 1;

	logF("Audio downloaded successfully; Beginning conversion...", end='', flush=True);
	__convertFile(audioInfo);


def getBestAudio(playlistVideo: PlaylistVideo) -> AudioInfo:
	allStreams: str = f"{getBaseUrl()}/streams/{playlistVideo.link}";
	logF(f"\n{playlistVideo.index} {playlistVideo.title} | Attempting to get highest quality audio... ", end='', flush=True);

	response: requests.Response = requests.get(allStreams);

	if (response.status_code == 500):
		raise Exception(response.json().get("message"));
	elif (response.status_code != 200):
		raise Exception("Failed to fetch video streams");
  
	data: dict = response.json();
	audioStreams: list = data.get("audioStreams", []);

	if (not audioStreams): # see if shit is empty
		raise Exception("No audio streams found!");

	# Find the audio stream with the highest bitrate
	bestStream = max(audioStreams, key=lambda stream: stream.get("bitrate", 0));
	logF(f"Found: {bestStream.get('mimeType')} {bestStream.get('quality')}", flush=True);

	# for Topic channels, remove the appeneded " - Topic" from the artist name
	uploaderName: str = data.get("uploader");
	if (uploaderName[-8:] == " - Topic"):
		uploaderName = uploaderName[:-8];

	return AudioInfo.fromPlaylistVideo(
		playlistVideo,
		bestStream.get("url"),
		removeIllegalChar(uploaderName)
	);