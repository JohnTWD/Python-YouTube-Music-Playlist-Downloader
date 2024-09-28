from os.path import abspath;

from dataclasses import dataclass
from classes.PlaylistVideo import PlaylistVideo;

from utils.miscUtils import logF;

@dataclass
class Playlist:
	name:       str;
	uploader:   str;
	videoCache: str; #file path to video list

	@staticmethod
	def getDetails(videoCachePath: str) -> list:
		info: list = ["link", "name", "author"];

		with open(videoCachePath, mode='r', encoding="UTF-8") as cache:
			info[0] = cache.readline().strip();
			info[1] = cache.readline().strip();
			info[2] = cache.readline().strip();
		cache.close();

		return info;

	@classmethod
	def loadCache(cls, videoCachePath: str) -> None:
		info: list = cls.getDetails(videoCachePath);
		return cls(info[1], info[2], abspath(videoCachePath)); # abspath because cwd changes
			 # name     uploader
			
	def eachInCache(self) -> PlaylistVideo:
		beginRead: bool = False;

		with open(self.videoCache, mode='r', encoding="UTF-8") as cache:
			for line in cache:
				if (beginRead):
					triArgs: tuple = tuple(line.strip().split(' ', 2));		# 2 splits only

					yield PlaylistVideo(
						int(triArgs[0]),	# index
						triArgs[2],			# title
						triArgs[1],			# link
					);
				else:
					beginRead = line.strip() == "---BEGIN PLAYLIST DATA (*DO NOT* EDIT THIS LINE)---";

	def show(self) -> None:
		logF("{:<10} - {:<40} - {:<20}".format("Index", "Title", "URL"));
		for video in self.eachInCache():
			assert isinstance(video, PlaylistVideo);
			logF("{:<10} - {:<40} - {:<20}".format(video.index, video.title, video.link));

	def getCount(self) -> int:
		count: int = 0;
		for _ in self.eachInCache():
			count += 1;
		return count;