import os;

homeDir: str = os.getcwd();
baseUrl: str = "https://pipedapi.syncpundit.io";

def setBaseUrl(newLink: str) -> None:
	global baseUrl;
	baseUrl = newLink;

def getBaseUrl() -> str:
	return baseUrl