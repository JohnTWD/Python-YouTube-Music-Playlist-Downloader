import os;
from constants import homeDir;
from utils.playlistParserUtils import PlaylistVideo;

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
