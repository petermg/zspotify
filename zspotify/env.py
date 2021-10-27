import os


def get_env(name, message, cast=str):
	if name in os.environ:
		return os.environ[name].strip()
	else:
		return message



_ROOT_PATH = "/download/ZSpotify Music/"
_ROOT_PODCAST_PATH = "ZSpotify Podcasts/"


ROOT_PATH = get_env('ROOT_PATH', _ROOT_PATH)
ROOT_PODCAST_PATH = get_env('ROOT_PODCAST_PATH', _ROOT_PODCAST_PATH)

DOWNLOAD_FORMAT = get_env('DOWNLOAD_FORMAT', 'mp3')

ANTI_BAN_WAIT_TIME = int(get_env('ANTI_BAN_WAIT_TIME', 1))
ANTI_BAN_WAIT_TIME_ALBUMS = int(get_env('ANTI_BAN_WAIT_TIME_ALBUMS', 30))
CHUNK_SIZE = get_env('CHUNK_SIZE', 50000)


SKIP_EXISTING_FILES = get_env('SKIP_EXISTING_FILES', True)
FORCE_PREMIUM = get_env('FORCE_PREMIUM', False)
OVERRIDE_AUTO_WAIT = get_env('OVERRIDE_AUTO_WAIT', False)
SPLIT_ALBUM_DISCS = get_env('SPLIT_ALBUM_DISCS', False)





