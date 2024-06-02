from dataclasses import dataclass;

from utils.miscUtils import logF;

@dataclass
class Playlist:
	name:     str;
	uploader: str;
	videos:   list; # PlaylistVideos

	def show(self) -> None:
		logF("{:<10} - {:<40} - {:<20}".format("Index", "Title", "URL"));
		for video in self.videos:
			logF("{:<10} - {:<40} - {:<20}".format(video.index, video.title, video.link));