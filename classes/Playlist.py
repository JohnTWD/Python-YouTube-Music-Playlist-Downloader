from dataclasses import dataclass;

@dataclass
class Playlist:
	name:     str;
	uploader: str;
	videos:   list; # PlaylistVideos

	def show(self) -> None:
		print("index    -   title   -   url");
		for video in self.videos:
			print(f"{video.index}   {video.title}   {video.link}");