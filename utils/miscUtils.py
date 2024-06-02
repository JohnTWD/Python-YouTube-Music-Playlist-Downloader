import os;
from constants import homeDir;

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