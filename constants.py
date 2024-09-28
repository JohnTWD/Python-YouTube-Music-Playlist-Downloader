import os;
from time import strftime;

homeDir: str = os.getcwd();
baseUrl: str = "https://pipedapi.adminforge.de";
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

class Bcolors: # thanks  https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

