# zspotify
Spotify song downloader without injecting into the windows client

```
Requirements:

Binaries

- Python 3.8 or greater
- ffmpeg*

Python packages:

- pip install -r requirements.txt

```
\*ffmpeg can be installed via apt for Debian-based distros or by downloading the binaries from [ffmpeg.org](https://ffmpeg.org) and placing them in your %PATH% in Windows.

- Use "-p" or "--playlist" to download a saved playlist from your account
- Use "-ls" or "--liked-songs" to download all the liked songs from your account
- Supply the URL or ID of a Track/Album/Playlist as an argument to download it
- Don't supply any arguments and it will give you a search input field to find and download a specific Track/Album/Playlist via the query.

- Change the MUSIC_FORMAT variable in zspotify.py to "ogg" if you rather that over "mp3"
- Change the FORCE_PREMIUM in zspotify.py to True if it is not automatically detecting your premium account.
- Change the RAW_AUDIO_AS_IS in zspotify.py to True if you wish to only save the raw audio stream without any re-encoding.

![image](https://user-images.githubusercontent.com/12180913/137978357-ee682c19-9a83-4820-82a1-7dad5230804c.png)

## **Docker:**
* docker run -it -v $(pwd)/docker/config:/config -v $(pwd)/docker/download:/download jsavargas/zspotify
* docker-compose run --rm zspotify



## **Changelog:**
**v1.6 (20 Oct 2021):**
- Added Pillow to requirements.txt.
- Removed websocket-client from requirements.txt because librespot-python added it to their dependency list.
- Made it hide your password when you type it in.
- Added manual override to force premium quality if zspotify cannot auto detect it.
- Added option to just download the raw audio with no re-encoding at all.
- Added Shebang line so it runs smoother on Linux.
- Made it download the entire track at once now so it is more efficent and fixed a bug users encountered.
- Added docker support

