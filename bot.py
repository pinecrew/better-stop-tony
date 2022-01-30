from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import config
import app


if __name__ == '__main__':
    updater = Updater(config.TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', app.start)
    dispatcher.add_handler(start_handler)

    msg_handler = MessageHandler(Filters.text & (~Filters.command), app.msg)
    dispatcher.add_handler(msg_handler)

    if config.USE_HEROKU:
        print('Start bot at Heroku')
        updater.start_webhook(
            listen='0.0.0.0', port=config.PORT, url_path=config.TOKEN,
            webhook_url=f'https://{config.APP}.herokuapp.com/{config.TOKEN}'
        )
    else:
        print('Start bot')
        updater.start_polling()
    updater.idle()
