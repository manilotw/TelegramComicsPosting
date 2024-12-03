import telegram
from environs import Env
from comics_functions import download_comics, get_comics_comment, delete_picture, get_random_comics

def main():

    env = Env()
    env.read_env()

    filename = 'comics.png'
    bot = telegram.Bot(token=env.str('TG_BOT_TOKEN'))
    chat_id = env.str('TG_CHAT_ID')

    random_comics_url = get_random_comics()

    download_comics(filename, random_comics_url)
    comics_comment = get_comics_comment(random_comics_url)
    
    with open(filename, 'rb') as image:
        bot.send_document(
            chat_id=chat_id,
            document=image,
            caption=comics_comment
        )
        
    delete_picture(filename)

if __name__ == '__main__':
    main()