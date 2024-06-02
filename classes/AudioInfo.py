from dataclasses import dataclass

from classes.PlaylistVideo import PlaylistVideo;

@dataclass
class AudioInfo(PlaylistVideo):
	url:    str;
	artist: str;

	@classmethod
	def fromPlaylistVideo(cls, plVid: PlaylistVideo, url: str, artist: str):
		return cls(plVid.index, plVid.title, plVid.link, url, artist);