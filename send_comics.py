import telegram
from environs import Env
from comics_functions import delete_picture, get_random_comics_num, download_picture, get_comics

def main():
    env = Env()
    env.read_env()

    filename = 'comics.png'
    bot = telegram.Bot(token=env.str('TG_BOT_TOKEN'))
    chat_id = env.str('TG_CHAT_ID')

    try:
        random_comics_url = get_random_comics_num()

        comics = get_comics(random_comics_url)
        download_picture(filename, comics['img'])
        comics_comment = comics['alt']
        
        with open(filename, 'rb') as image:
            bot.send_document(
                chat_id=chat_id,
                document=image,
                caption=comics_comment
            )
    finally:
        delete_picture(filename)

if __name__ == '__main__':
    main()
