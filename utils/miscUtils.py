import os;
import re;

from constants import homeDir;
from classes.PlaylistVideo import PlaylistVideo;


__illegalCharRegex: re.Pattern = re.compile(r"[\/*?:\"<>|]");
def removeIllegalChar(sus: str) -> str:
	return re.sub(__illegalCharRegex, '', sus);

def makeFolderEnter(folderName: str) -> None:
	try:
		os.mkdir(folderName);
		print(f"successful creation of {folderName}");
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
		print(f"Found existing temp file, removing {fileInPath}");
		os.remove(fileInPath);

	if (os.path.exists(fileOutPath)):
		print(f"File already exists, skipping download ({plVid.index} : {plVid.title})");
		return False;

	return True;

def makeFolder(folderName: str) -> None:
	try:
		os.mkdir(folderName);
		print(f"successful creation of {folderName}");
	except FileExistsError:
		pass;

def logF(fileName: str, output: str, end: str = '\n', flush: bool = False) -> None:
	with open(os.path.join(homeDir, "logs", fileName), mode='a', encoding="UTF-8") as txt:
		print(text, file=txt, end=end, flush=flush);
		print(text, end=end, flush=flush);
