#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import keyboard
import requests
import warnings
import asyncio
from shazamio import Shazam
from audio_extract import extract_audio

warnings.filterwarnings("ignore")


# In[ ]:


class Song_Info:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

def song_to_dict(song_info):
    return {
        'song': song_info.title,
        'artist': song_info.artist
    }


# In[ ]:


def cnv_audio(in_file, out_file):
    print(in_file, out_file)
    extract_audio(input_path=in_file,
                  output_path=out_file,
                  overwrite=True)   


# In[ ]:


def read_sample(buffer_file):
    stream_url = 'https://az10.yesstreaming.net/radio/8060/radio.mp3'
    i = 1
    with requests.get(stream_url, stream=True, timeout=5.0) as response:
        with open(buffer_file, 'wb') as sample_file:
            for chunk in response.iter_content(chunk_size=10000):
                if  i > 300:
                    break
                sample_file.write(chunk)
                i+=1


# In[ ]:


async def shazam_it(music_file):
    shazam = Shazam()
    out = await shazam.recognize(music_file)
    return out


# In[ ]:


def add_it_to_db(db_name, a_song):
    with open(db_name, 'a') as db_file:
        json.dump(a_song, db_file, default=song_to_dict)
        db_file.write('\n')


# In[ ]:


async def start_spy():
    file_for_buffer = r".\buffer.aac"
    file_for_mp3 = r".\buffer.mp3"
    station = "RockFM.json"
    prev_song = ""
    prev_artist = ""
    while True:
        read_sample(file_for_buffer)
        cnv_audio(file_for_buffer, file_for_mp3)
        shazam_chars =  await shazam_it(file_for_mp3)
        if len(shazam_chars["matches"]) != 0:
            sample_song = shazam_chars['track']['title']
            sample_artist = shazam_chars['track']['subtitle']
            song = Song_Info(sample_song, sample_artist)
            if prev_song != sample_song:
                add_it_to_db(station, song)
                print('Added ' + song.title, song.artist)
                prev_song = sample_song
            if keyboard.is_pressed("q"):
                break      


# In[ ]:

if __name__ == "__main__":
    asyncio.run(start_spy())





