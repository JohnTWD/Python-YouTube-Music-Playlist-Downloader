from classes.Playlist import Playlist;
from constants import Bcolors;

# probably super inefficient, but i just want to get this done

def __displayDetails(path: str) -> None:
	details: list = Playlist.getDetails(path);
	print(Bcolors.OKCYAN + f"{path}\nLink: {details[0]}\nName: {details[1]}\nAuthor: {details[2]}\n------" + Bcolors.ENDC);

def __getPlaylistSongs(path: str) -> set:
	playlist: Playlist = Playlist.loadCache(path);
	__displayDetails(path);

	rtn: set = set();
	for i in playlist.eachInCache():
		rtn.add(i.title);

	return rtn;

def __displayDiff(diff: set, sign: str) -> None:
	for title in diff:
		print(f"{sign} {title}" + Bcolors.ENDC);

def comparePlaylistData(filePath1: str, filePath2: str) -> None:
	priPL: set = __getPlaylistSongs(filePath1);
	secPL: set = __getPlaylistSongs(filePath2);

	missing: set = priPL - secPL;
	new:	 set = secPL - priPL;

	__displayDiff(new, f"{Bcolors.OKGREEN} +");
	__displayDiff(missing, f"{Bcolors.FAIL} -");