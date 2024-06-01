import os;
from constants import homeDir;

def makeFolderEnter(folderName: str) -> None:
  try:
    os.mkdir(folderName);
    print(f"successful creation of {folderName}");
    os.chdir(
        os.path.join(os.curdir, folderName)
    );
  except FileExistsError:
    pass;

def goHome() -> None:
  os.chdir(homeDir);

