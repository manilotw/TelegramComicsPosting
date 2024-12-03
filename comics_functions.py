import requests
import random
import os

def download_picture(filename, url):
    response = requests.get(url)
    response.raise_for_status()

    with open (filename, 'wb') as file:
        file.write(response.content)

def get_random_comics():

    last_comics_url = 'https://xkcd.com/info.0.json'

    response = requests.get(last_comics_url)
    response.raise_for_status()
    last_comics = response.json()
    last_comics_num = last_comics['num']

    random_comics_num = random.randint(1, last_comics_num)

    return f'https://xkcd.com/{random_comics_num}/info.0.json'

def download_comics(filename, random_comics_url):

    response = requests.get(random_comics_url)
    response.raise_for_status()
    comics = response.json()
    comics_photo = comics['img']

    return download_picture(filename, comics_photo)

def get_comics_comment(random_comics_url):

    response = requests.get(random_comics_url)
    response.raise_for_status()
    comics = response.json()
    comics_comment = comics['alt']

    return comics_comment

def delete_picture(filename):

    if os.path.exists(filename):
        os.remove(filename)

def main():
    filename = 'comics.png'
    random_comics_url = get_random_comics()

    download_comics(filename, random_comics_url)
    get_comics_comment(random_comics_url)
    delete_picture(filename)
    
if __name__ == '__main__':
    main()