import requests;
import os;
import re;
from subprocess import call;
from dataclasses import dataclass;

from constants import getBaseUrl;

@dataclass
class AudioInfo:
	url:    str;
	title:  str;
	artist: str;

def __removeIllegalChar(string: str) -> str:
	return re.sub(r"[\\/*?:\"<>|]", '', str)

def __convertFile(audioInfo: AudioInfo) -> None:
	fileInPath:  str = os.path.join(os.getcwd(), audioInfo.title + ".temp");
	fileOutPath: str = os.path.join(os.getcwd(), audioInfo.title + ".mp3");
	
	# the actual conversion
	command: str = ["ffmpeg", "-i" ,  fileInPath, "-metadata", f"artist={audioInfo.artist}", fileOutPath];
	call(command);

	if (os.path.exists(fileOutPath)):
		os.remove(fileInPath)   # get rid of the original file
		print(f'Converted: {fileOutPath} to MP3');
	else:
		raise Exception("Something went wrong with conversion. Leaving temp file alone...");


def downloadAudio(audioInfo: AudioInfo) -> None:
	print("Beginning download...", end="", flush=True);
	filePath: str = os.path.join(os.getcwd(), audioInfo.title, + ".temp");

	with requests.get(audioInfo.url, stream=True) as r:
		r.raise_for_status();

		with open(filePath, "wb") as f:
			i: int = 0;
			for chunk in r.iter_content(chunk_size=8192):
				if (i >= 50):
					print('.', end='', flush=True);
					i = 0;
				f.write(chunk);
				i += 1;

	print(f"Audio downloaded successfully: @{filePath} \nBeginning conversion...", end='', flush=True);
	__convertFile(audioInfo);


def getBestAudio(idVideo: str) -> AudioInfo:
	allStreams: str = f"{getBaseUrl()}/streams/{idVideo}";
	print("Attempting to get highest quality audio... ", end='', flush=True);

	response: requests.Response = requests.get(allStreams);
	if (response.status_code != 200):
		raise Exception("Failed to fetch video streams");
  
	data: dict = response.json();
	audioStreams: list = data.get("audioStreams", []);

	if (not audioStreams): # see if shit is empty
		raise Exception("No audio streams found!");

	# Find the audio stream with the highest bitrate
	bestStream = max(audioStreams, key=lambda stream: stream.get("bitrate", 0));
	print(f"Found: {bestStream.get('mimeType')} {bestStream.get('quality')}", flush=True);
  
	return AudioInfo(
		bestStream.get("url"),
		__removeIllegalChar(data.get("title")), 
		__removeIllegalChar(data.get("uploader"))
	);