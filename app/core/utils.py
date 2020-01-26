import requests
import base64

def get_lyrics(lyrics):

    if lyrics is not None:
        data = {
            'q': str(lyrics),
            'return':'timecode,apple_music,deezer,spotify',
            'api_token': 'f2459ae0fc49b06829ff9f11085b9cfa'
            }
    result = requests.post('https://api.audd.io/findLyrics/', data=data)

    result = result.json().get('result')

    artists = []

    if len(result) > 0:
        for result_item in result:
            current_lyrics = result_item.get('lyrics').strip()
            if lyrics.lower().strip() in current_lyrics.lower():
                artists.append(
                    {'track_title': result_item.get('title'),
                    'track_artist': result_item.get('artist')
                    })

    artist = None
    search_id = None


    for artist_item in artists:
        artist = artist_item.get('track_artist')
        title = artist_item.get('track_title')
        search_id = requests.get(f'https://api.deezer.com/search?q={artist}')

        data = search_id.json().get('data')
        if len(data) > 0:
            for data_item in data:
                title_data = data_item.get('title')
                artist_data = data_item.get('artist')
                if artist_data.get('name').lower() == artist.lower():
                    if title_data is not None and title is not None:
                        if title_data.lower() in title.lower() or title.lower() in title_data.lower():
                            return data_item.get("id")


def get_audio_file(audio_link):

    header, encoded = audio_link.split(",", 1)

    data = base64.b64decode(encoded)
    with open('./core/static/media/demo10', 'wb') as file:
        file.write(data)

    data = {
        'return': 'timecode,apple_music,deezer,spotify',
        'api_token': 'f9d05c0e0df19edf712ee220b4e30cac'
    }
    result = requests.post('https://api.audd.io/', data=data, files={'file': open('./core/static/media/demo10', 'rb') })
    return result.json()
