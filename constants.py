import os;
from time import strftime;

homeDir: str = os.getcwd();
baseUrl: str = "https://pipedapi.syncpundit.io";
timeStamp: str = strftime("%Y-%b-%d-%H-%M-%S");

def setBaseUrl(newLink: str) -> None:
	global baseUrl;
	baseUrl = newLink;

def getBaseUrl() -> str:
	return baseUrl;

def setTimeStamp() -> None:
	global timeStamp;
	timeStamp = strftime("%Y-%b-%d-%H-%M-%S");

def getTimeStamp() -> str:
	return timeStamp;
