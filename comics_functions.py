import requests
import random
import os

def download_picture(filename, url):
    response = requests.get(url)
    response.raise_for_status()

    with open (filename, 'wb') as file:
        file.write(response.content)

def get_random_comics_num():

    last_comics_url = 'https://xkcd.com/info.0.json'

    response = requests.get(last_comics_url)
    response.raise_for_status()
    last_comics = response.json()
    last_comics_num = last_comics['num']

    random_comics_num = random.randint(1, last_comics_num)

    return f'https://xkcd.com/{random_comics_num}/info.0.json'

def get_comics(random_comics_url):
    response = requests.get(random_comics_url)
    response.raise_for_status()
    comics = response.json()

    return comics

def delete_picture(filename):

    if os.path.exists(filename):
        os.remove(filename)
