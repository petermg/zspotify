import re 
import os 

from tqdm import tqdm

from const import ITEMS, ARTISTS, NAME, ID
from track import download_track
from utils import fix_filename, wait
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
    release_date = re.search('(\d{4})', resp['release_date']).group(1)
    return resp[ARTISTS][0][NAME], fix_filename(resp[NAME]), release_date


def get_artist_albums(artist_id):
    """ Returns artist's albums """
    resp = ZSpotify.invoke_url(f'{ARTIST_URL}/{artist_id}/albums?include_groups=album%2Csingle')
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
    artist, album_name, album_release_date = get_album_name(album)
    artist_fixed = fix_filename(artist)
    album_name_fixed = fix_filename(album_name)
    tracks = get_album_tracks(album)

    disc_number_flag = False
    for track in tracks:
        if track['disc_number'] > 1:
            disc_number_flag = True


    if disc_number_flag:
        for n, track in tqdm(enumerate(tracks, start=1), unit_scale=True, unit='Song', total=len(tracks)):
            disc_number = str(track['disc_number']).zfill(2)
            download_track(track[ID], os.path.join(artist_fixed, f"({album_release_date}) - {album_name_fixed}", f"CD {disc_number}"),prefix=True, prefix_value=str(n), disable_progressbar=True)
    else: 

        for n, track in tqdm(enumerate(tracks, start=1), unit_scale=True, unit='Song', total=len(tracks)):
            download_track(track[ID], f'{artist_fixed}/({album_release_date}) - {album_name_fixed}',
                       prefix=True, prefix_value=str(n), disable_progressbar=True)


def download_artist_albums(artist):
    """ Downloads albums of an artist """
    albums = get_albums_artist(artist)
    i=0

    print("\n\tALL ALBUMS: ",len(albums)," IN:",str(set(album['album_type'] for album in albums)))

    for album in albums:
        if artist == album[ARTISTS][0][ID] and album['album_type'] != 'single':
            i += 1
            year = re.search('(\d{4})', album['release_date']).group(1)
            print(f" {i} {album[ARTISTS][0][NAME]} - ({year}) {album[NAME]} [{album['total_tracks']}] [{album['album_type']}] [{album[ID]}]")
    total_albums_downloads = i
    print("\n")

    wait(10)

    i=0
    for album in albums:
        if artist == album[ARTISTS][0]['id'] and album['album_type'] != 'single' :
            i += 1
            year = re.search('(\d{4})', album['release_date']).group(1)
            print(f"\n\n\n{i}/{total_albums_downloads} {album[ARTISTS][0][NAME]} - ({year}) {album[NAME]} [{album['total_tracks']}]")
            download_album(album['id'])
