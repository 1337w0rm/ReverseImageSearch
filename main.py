import requests
import logging
from telegram.ext import Updater, CommandHandler
from config import Config
from upload import upload
from webscreenshot.webscreenshot import *
import argparse
from glob import glob



#Logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


updater = Updater(token = Config.BOT_TOKEN, use_context=True)
dp = updater.dispatcher

mode="prod"

if mode == "dev":
    def run(updater):
        updater.start_polling()
elif mode == "prod":
    def run(updater):
        PORT = int(os.environ.get("PORT", "8443"))
        # Code from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=Config.BOT_TOKEN)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(Config.HEROKU_APP_NAME, Config.BOT_TOKEN))



def yfind(update, context):
	fileId = update.message.reply_to_message.photo[0].file_id
	file = context.bot.getFile(fileId)
	file.download('ss.jpg')

	imageLink = upload()

	query = list()
	query.append("https://yandex.com/images/search?url=" + imageLink + "&rpt=imageview")

	options = argparse.Namespace(URL=None, ajax_max_timeouts='1400,1800', cookie=None, crop="10,20,w,h", format='png', header=None, http_password=None, http_username=None, imagemagick_binary=None, input_file=None, label=False, label_bg_color='NavajoWhite', label_size=60, log_level='NOTSET', multiprotocol=False, no_xserver=False, output_directory='screenshots', port=None, proxy=None, proxy_auth=None, proxy_type=None, quality=75, renderer='phantomjs', renderer_binary=None, ssl=False, timeout=30, verbosity=2, window_size='1200,800', workers=1)
	take_screenshot(query, options)

	for i in glob('screenshots/*.png'):
		try:
			context.bot.send_photo(chat_id=update.message.chat_id, photo=open(i, 'rb'), caption=query[0], timeout = 120)
			os.remove(i)
		except :
			context.bot.send_document(chat_id=update.message.chat_id, document=open(i, 'rb'), caption=query[0], timeout = 120)
			os.remove(i)
def gfind(update, context):
	fileId = update.message.reply_to_message.photo[0].file_id
	file = context.bot.getFile(fileId)
	file.download('ss.jpg')

	imageLink = upload()

	query = list()
	query.append("https://images.google.com/searchbyimage?image_url=" + imageLink)

	options = argparse.Namespace(URL=None, ajax_max_timeouts='1400,1800', cookie=None, crop="5,20,w,h", format='png', header=None, http_password=None, http_username=None, imagemagick_binary=None, input_file=None, label=False, label_bg_color='NavajoWhite', label_size=60, log_level='NOTSET', multiprotocol=False, no_xserver=False, output_directory='screenshots', port=None, proxy=None, proxy_auth=None, proxy_type=None, quality=75, renderer='phantomjs', renderer_binary=None, ssl=False, timeout=30, verbosity=2, window_size='1200,800', workers=1)
	take_screenshot(query, options)

	for i in glob('screenshots/*.png'):
		try:
			context.bot.send_photo(chat_id=update.message.chat_id, photo=open(i, 'rb'), caption=query[0], timeout = 120)
			os.remove(i)
		except :
			context.bot.send_document(chat_id=update.message.chat_id, document=open(i, 'rb'), caption=query[0], timeout = 120)
			os.remove(i)



def main():
	dp.add_handler(CommandHandler("yfind", yfind))
	dp.add_handler(CommandHandler("gfind", gfind))
	logging.info("Bot started")
	run(updater)

if __name__ == '__main__':
    main()