from dataclasses import dataclass;

@dataclass
class Playlist:
	name:     str;
	uploader: str;
	videos:   list; # PlaylistVideos

	def show(self) -> None:
		print("{:<10} - {:<40} - {:<20}".format("Index", "Title", "URL"));
		for video in self.videos:
			print("{:<10} - {:<40} - {:<20}".format(video.index, video.title, video.link));