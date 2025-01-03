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


def add_it_to_db_old(db_name, a_song, an_artist):
    info_dict ={}
    info_dict["song"] = a_song
    info_dict["artist"] = an_artist
    json_info = json.dumps(info_dict)
    with open(db_name, 'a') as db_file:
        json.dump(json_info, db_file, indent=3) 


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


file_for_buffer = r".\buffer.acc"
file_for_mp3 = r".\mp3_file.mp3"
#cnv_audio(file_for_buffer, file_for_mp3)
print(file_for_buffer, file_for_mp3)


# In[ ]:


await start_spy()


# In[ ]:


SUPPORTED_FFMPEG_FORMATS


# In[ ]:


shazam_chars = shazam_it(r".\buffer.mp3")


# In[ ]:


shazam_chars =  await shazam_it(r".\buffer.mp3")


# In[ ]:


print(shazam_chars)


# In[ ]:


print(len(shazam_chars["matches"]))


# In[ ]:


loop.run_until_complete(shazam_it)


# In[ ]:


import sys
print(sys.version)


# In[ ]:




