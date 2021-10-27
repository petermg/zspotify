import os


def get_env(name, message, cast=str):
	if name in os.environ:
		return os.environ[name].strip()
	else:
		return message



SANITIZE = ('\\', '/', ':', '*', '?', '\'', '<', '>', '"')

SAVED_TRACKS_URL = 'https://api.spotify.com/v1/me/tracks'

TRACKS_URL = 'https://api.spotify.com/v1/tracks'

TRACKNUMBER = 'tracknumber'

TOTAL_TRACKS = 'total_tracks'

DISCNUMBER = 'discnumber'

YEAR = 'year'

ALBUM = 'album'

ALBUM_TYPE = 'album_type'

TRACKTITLE = 'tracktitle'

ARTIST = 'artist'

ARTISTS = 'artists'

ARTWORK = 'artwork'

TRACKS = 'tracks'

TRACK = 'track'

ITEMS = 'items'

NAME = 'name'

GENRES = 'genres'

ID = 'id'

URL = 'url'

RELEASE_DATE = 'release_date'

IMAGES = 'images'

LIMIT = 'limit'

OFFSET = 'offset'

AUTHORIZATION = 'Authorization'

IS_PLAYABLE = 'is_playable'

TRACK_NUMBER = 'track_number'

DISC_NUMBER = 'disc_number'

SHOW = 'show'

ERROR = 'error'

EXPLICIT = 'explicit'

PLAYLIST = 'playlist'

PLAYLISTS = 'playlists'

OWNER = 'owner'

DISPLAY_NAME = 'display_name'

ALBUMS = 'albums'

TYPE = 'type'

PREMIUM = 'premium'

USER_READ_EMAIL = 'user-read-email'

PLAYLIST_READ_PRIVATE = 'playlist-read-private'

WINDOWS_SYSTEM = 'Windows'

CREDENTIALS_JSON = 'credentials.json'

CONFIG_FILE_PATH = '../zs_config.json'

ROOT_PATH = 'ROOT_PATH'

ROOT_PODCAST_PATH = 'ROOT_PODCAST_PATH'

SKIP_EXISTING_FILES = 'SKIP_EXISTING_FILES'

DOWNLOAD_FORMAT = 'DOWNLOAD_FORMAT'

FORCE_PREMIUM = 'FORCE_PREMIUM'

ANTI_BAN_WAIT_TIME = 'ANTI_BAN_WAIT_TIME'

ANTI_BAN_WAIT_TIME_ALBUMS = 'ANTI_BAN_WAIT_TIME_ALBUMS'

OVERRIDE_AUTO_WAIT = 'OVERRIDE_AUTO_WAIT'

CHUNK_SIZE = 'CHUNK_SIZE'

SPLIT_ALBUM_DISCS = 'SPLIT_ALBUM_DISCS'

SEARCH_LIMIT = 'SEARCH_LIMIT'

_ROOT_PATH = "/download/ZSpotify Music/"
_ROOT_PODCAST_PATH = "/download/ZSpotify Podcasts/"

CONFIG_DEFAULT_SETTINGS = {
    'ROOT_PATH': get_env('ROOT_PATH', _ROOT_PATH),
    'ROOT_PODCAST_PATH': get_env('ROOT_PODCAST_PATH', _ROOT_PODCAST_PATH),
    'SKIP_EXISTING_FILES': get_env('SKIP_EXISTING_FILES', True),
    'DOWNLOAD_FORMAT': get_env('DOWNLOAD_FORMAT', 'mp3'),
    'ANTI_BAN_WAIT_TIME': int(get_env('ANTI_BAN_WAIT_TIME', 1)),
    'ANTI_BAN_WAIT_TIME_ALBUMS': int(get_env('ANTI_BAN_WAIT_TIME_ALBUMS', 30)),
    'SEARCH_LIMIT': int(get_env('SEARCH_LIMIT', 10)),
    'FORCE_PREMIUM': False,
    'OVERRIDE_AUTO_WAIT': False,
    'CHUNK_SIZE': 50000,
    'SPLIT_ALBUM_DISCS': False
}


