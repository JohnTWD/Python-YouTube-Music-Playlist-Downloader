import os;
import re;

from constants import homeDir, getTimeStamp;
from classes.PlaylistVideo import PlaylistVideo;


__illegalCharRegex: re.Pattern = re.compile(r"[\/*?:\"<>|]");
def removeIllegalChar(sus: str) -> str:
	return re.sub(__illegalCharRegex, '', sus);

def makeFolderEnter(folderName: str) -> None:
	try:
		os.mkdir(folderName);
		logF(f"successful creation of {folderName}");
	except FileExistsError:
		pass;
	
	os.chdir(
		os.path.join(os.curdir, folderName)
	);

def goHome() -> None:
	os.chdir(homeDir);

def handleExistingDownloads(plVid: PlaylistVideo) -> bool:
	fileInPath:  str = os.path.join(os.getcwd(), plVid.title + ".temp");
	fileOutPath: str = os.path.join(os.getcwd(), plVid.title + ".mp3");

	if (os.path.exists(fileInPath)):
		logF(f"Found existing temp file, removing {fileInPath}");
		os.remove(fileInPath);

	if (os.path.exists(fileOutPath)):
		logF(f"File already exists, skipping download ({plVid.index} : {plVid.title})");
		return False;

	return True;

def makeFolder(folderName: str, shutUp: bool = False) -> None:
	try:
		os.mkdir(folderName);

		if (not shutUp):
			logF(f"successful creation of {folderName}");
	except FileExistsError:
		pass;

def logF(
		output:   str, 
		end:      str = '\n', 
		flush:    bool = False, 
		console:  bool = True, 
		fileName: str = "console"
	) -> None:

	with open(os.path.join(homeDir, "logs", getTimeStamp(), fileName + ".txt"), mode='a', encoding="UTF-8") as txt:
		print(output, file=txt, end=end, flush=flush);
		if (console):
			print(output, end=end, flush=flush);