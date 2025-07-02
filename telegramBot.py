#telegram bot\
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '7750632666:AAGXcXKo8Y6ek1PwN2RNJTbZsjmU_VO1AoU'
BOT_USERNAME: Final = '@lekhansh_khileshwari_bot'

#COMMANDS
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with us! We are LEKHANSH & KHILESHWARI ')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am TELEGRAM BOT, Please type something to receive respond')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is custom command!!')

#RESPONSES
def handle_response(text: str) -> str:
    processed: str = text.lower()


    if 'hello' in processed:
        return 'Hey There!'
    if 'how are you' in processed:
        return 'I am good'
    if 'I Love Python' in processed:
        return 'Remember to grasp ideas'
    if 'adarsh' in processed:
        return 'hi adarsh nice to meet you'

    return 'I dont understand what you wrote...'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return()
    else:
        response: str = handle_response(text)

    print('Bot: ', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':

    print('STARTING BOT....')
    app = Application.builder().token(TOKEN).build()

    #COMMANDS
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #MESSAGES
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #ERROR
    app.add_error_handler(error)

    #POLLS THE BOT
    print('POLLING BOT....')
    app.run_polling(poll_interval=3)
    
    
