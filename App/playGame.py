import os
import requests
from random_word import RandomWords

r = RandomWords()

url = "https://voicerss-text-to-speech.p.rapidapi.com/"

querystring = {"key":"08e279563d9d48f186479bf7d32ffd98","src":r.get_random_word(),"hl":"en-us","r":"0","c":"mp3","f":"8khz_8bit_mono"}

headers = {
    "X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com",
    "X-RapidAPI-Key": "e9c232a02cmsh24b624b46bb82b4p1a63fdjsne3b7c720565c"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)