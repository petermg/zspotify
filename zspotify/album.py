import re 
import os 

from tqdm import tqdm

from const import ITEMS, ARTISTS, NAME, ID, TOTAL_TRACKS, ALBUM_TYPE, DISC_NUMBER, ANTI_BAN_WAIT_TIME_ALBUMS
from track import download_track
from utils import sanitize_data, wait
from zspotify import ZSpotify

ALBUM_URL = 'https://api.spotify.com/v1/albums'
ARTIST_URL = 'https://api.spotify.com/v1/artists'


def get_album_tracks(album_id):
    """ Returns album tracklist """
    songs = []
    offset = 0
    limit = 50

    while True:
        resp = ZSpotify.invoke_url_with_params(f'{ALBUM_URL}/{album_id}/tracks', limit=limit, offset=offset)
        offset += limit
        songs.extend(resp[ITEMS])
        if len(resp[ITEMS]) < limit:
            break

    return songs


def get_album_name(album_id):
    """ Returns album name """
    resp = ZSpotify.invoke_url(f'{ALBUM_URL}/{album_id}')
    return resp[ARTISTS][0][NAME], re.search('(\d{4})', resp['release_date']).group(1),sanitize_data(resp[NAME]),resp[TOTAL_TRACKS]


def get_artist_albums(artist_id):
    """ Returns artist's albums """
    offset = 0
    limit = 50
    include_groups = 'album,compilation'

    resp = ZSpotify.invoke_url_with_params(f'{ARTIST_URL}/{artist_id}/albums',limit=limit, offset=offset, include_groups=include_groups)
    # Return a list each album's id
    album_ids = [resp[ITEMS][i][ID] for i in range(len(resp[ITEMS]))]
    # Recursive requests to get all albums including singles an EPs
    while resp['next'] is not None:
        resp = ZSpotify.invoke_url(resp['next'])
        album_ids.extend([resp[ITEMS][i][ID] for i in range(len(resp[ITEMS]))])

    return album_ids

def get_albums_artist(artists_id):
    """ returns list of albums in a artist """

    offset = 0
    limit = 50
    include_groups = 'album,compilation'

    params = {'limit': limit, 'include_groups': include_groups, 'offset': offset}

    resp = ZSpotify.invoke_url_with_params(f'{ARTIST_URL}/{artists_id}/albums',limit=limit, offset=offset, include_groups=include_groups)
    album_ids = [resp[ITEMS][i] for i in range(len(resp[ITEMS]))]

    while resp['next'] is not None:
        resp = ZSpotify.invoke_url(resp['next'])
        album_ids.extend([resp[ITEMS][i] for i in range(len(resp[ITEMS]))])

    return album_ids


def download_album(album):
    """ Downloads songs from an album """
    artist, album_release_date, album_name, total_tracks = get_album_name(album)
    tracks = get_album_tracks(album)

    disc_number_flag = False
    for track in tracks:
        if track[DISC_NUMBER] > 1:
            disc_number_flag = True

    if disc_number_flag: 
        for n, track in tqdm(enumerate(tracks, start=1), unit_scale=True, unit='Song', total=len(tracks)):
            disc_number = str(track[DISC_NUMBER]).zfill(2)
            download_track(track[ID], os.path.join(artist, f"{artist} - ({album_release_date}) - {album_name}", f"CD {disc_number}"),prefix=True, prefix_value=str(n), disable_progressbar=True)
    else: 
        for n, track in tqdm(enumerate(tracks, start=1), unit_scale=True, unit='Song', total=len(tracks)):
            download_track(track[ID], os.path.join(artist, f"{artist} - ({album_release_date}) - {album_name}"),prefix=True, prefix_value=str(n), disable_progressbar=True)



def download_artist_albums(artist):
    """ Downloads albums of an artist """
    albums = get_albums_artist(artist)
    i=0

    print("\n\tALL ALBUMS: ",len(albums)," IN:",str(set(album[ALBUM_TYPE] for album in albums)))

    for album in albums:
        if artist == album[ARTISTS][0][ID] and album[ALBUM_TYPE] != 'single':
            i += 1
            year = re.search('(\d{4})', album['release_date']).group(1)
            print(f" {i} {album[ARTISTS][0][NAME]} - ({year}) {album[NAME]} [{album[TOTAL_TRACKS]}] [{album[ALBUM_TYPE]}] [{album[ID]}]")
    total_albums_downloads = i
    print("\n")
    wait(10)

    i=0
    for album in albums:
        if artist == album[ARTISTS][0]['id'] and album[ALBUM_TYPE] != 'single' :
            i += 1
            year = re.search('(\d{4})', album['release_date']).group(1)
            print(f"\n\n\n{i}/{total_albums_downloads} {album[ARTISTS][0][NAME]} - ({year}) {album[NAME]} [{album[TOTAL_TRACKS]}]")
            download_album(album['id'])
            wait(ZSpotify.get_config(ANTI_BAN_WAIT_TIME_ALBUMS))


