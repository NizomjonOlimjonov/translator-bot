import telebot
import database
import buttons

TOKEN = '6320130895:AAEf1eOxKFyBddmaZcH6n6GdblTDoHdQP9w'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
        user = database.check_user(message.from_user.id)
        if user:
            bot.send_message(message.from_user.id, 'To start translate , user the button',reply_markup=buttons.translate_button())
        else:
            bot.send_message(message.from_user.id,'To start the using the bot,share your contact',reply_markup=buttons.contact_button())
            bot.register_next_step_handler(message,get_contact)
def get_contact(message):
        if message.contact:
            
            user_phone = message.contact.phone_number
            first_name = message.contact.first_name
            telegram_id = message.from_user.id

            database.register_user(telegram_id,user_phone,first_name)
            bot.send_message(message.from_user.id,'To start translate , user the button',reply_markup=buttons.translate_button())

        else:
            bot.send_message(message.from_user.id,'Please to share your contact use the button', reply_markup=buttons.contact_button())
            bot.register_next_step_handler(message,get_contact)
bot.polling()



