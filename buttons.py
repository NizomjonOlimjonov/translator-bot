from telebot.types  import ReplyKeyboardMarkup , KeyboardButton

def contact_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Share contact ',request_contact=True)

    kb.add(button)
    return kb 
def translate_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('Translate')
    kb.add(button1)
    return kb
translate_button()

def language_buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    ru = KeyboardButton('Ru')
    uz = KeyboardButton('Uz')
    en = KeyboardButton('En')
    es = KeyboardButton('Es')
    fr = KeyboardButton('Fr')
    ar = KeyboardButton('Ar')
    kb.add(ru,uz,en,es,fr,ar)
    return kb
