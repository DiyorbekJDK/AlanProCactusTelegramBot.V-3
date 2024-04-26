import telebot
from data.util.tokens import bot_token
import sqlite3
from telebot import types
from data.locale.global_text import *
from data.util.links import *
from data.locale.rus_locale import *
from data.locale.eng_locale import *
from data.locale.uzb_locale import *
from data.locale.kzkh_locale import *
from data.locale.tajik_locale import *

bot = telebot.TeleBot(bot_token)


#################
# Bot functions #
#################


def sendErrorToOwner(mess):
    send_message(owner_id, mess)


# Sends simple message to user
def send_message(chat_id, mess, parseMode=''):
    bot.send_message(chat_id, mess, parseMode)


# Sends message with the markup to connect buttons
def send_button_message(chat_id, mess, replyMarkup: types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup):
    bot.send_message(chat_id=chat_id, text=mess, reply_markup=replyMarkup)


# Creates inline keyboard button
def createButton(buttonText, buttonLink):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=buttonText, url=buttonLink))
    return markup


# Creates more inline keyboard buttons
def createMoreButtons(buttonsCount: int = 2, button1Text="", button1Link="", button2Text="", button2Link="",
                      button3Text="", button3Link="", button4Text="", button4Link=""):
    mark = types.InlineKeyboardMarkup()
    if buttonsCount == 2:
        btn = types.InlineKeyboardButton(button1Text, button1Link)
        btn2 = types.InlineKeyboardButton(button2Text, button2Link)
        mark.add(btn, btn2)
        return mark
    elif buttonsCount == 3:
        btn = types.InlineKeyboardButton(button1Text, button1Link)
        btn2 = types.InlineKeyboardButton(button2Text, button2Link)
        btn3 = types.InlineKeyboardButton(button3Text, button3Link)
        mark.add(btn, btn2, btn3)
        return mark
    elif buttonsCount == 4:
        btn = types.InlineKeyboardButton(button1Text, button1Link)
        btn2 = types.InlineKeyboardButton(button2Text, button2Link)
        btn3 = types.InlineKeyboardButton(button3Text, button3Link)
        btn4 = types.InlineKeyboardButton(button4Text, button4Link)
        mark.add(btn, btn2, btn3, btn4)
        return mark
    else:
        print("InlineKeyboard button error")


# Creates keyboard buttons
def createKeyboardButtons(buttonsCount: int = 2, resizeKeyboard: bool = False, rowWidth: int = 2, button1Text="",
                          button2Text="", button3Text="", button4Text="", button5Text="", button6Text="",
                          button7Text="", button8Text="", button9Text=""):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=resizeKeyboard, row_width=rowWidth)
    if buttonsCount == 2:
        btn = types.InlineKeyboardButton(button1Text)
        btn2 = types.InlineKeyboardButton(button2Text)
        markup.add(btn, btn2)
        return markup
    elif buttonsCount == 1:
        btn = types.InlineKeyboardButton(button1Text)
        markup.add(btn)
        return markup
    elif buttonsCount == 3:
        btn = types.InlineKeyboardButton(button1Text)
        btn2 = types.InlineKeyboardButton(button2Text)
        btn3 = types.InlineKeyboardButton(button3Text)
        markup.add(btn, btn2, btn3)
        return markup
    elif buttonsCount == 4:
        btn = types.InlineKeyboardButton(button1Text)
        btn2 = types.InlineKeyboardButton(button2Text)
        btn3 = types.InlineKeyboardButton(button3Text)
        btn4 = types.InlineKeyboardButton(button4Text)
        markup.add(btn, btn2, btn3, btn4)
        return markup
    elif buttonsCount == 5:
        btn = types.InlineKeyboardButton(button1Text)
        btn2 = types.InlineKeyboardButton(button2Text)
        btn3 = types.InlineKeyboardButton(button3Text)
        btn4 = types.InlineKeyboardButton(button4Text)
        btn5 = types.InlineKeyboardButton(button5Text)
        markup.add(btn, btn2, btn3, btn4, btn5)
        return markup
    elif buttonsCount == 6:
        btn = types.InlineKeyboardButton(button1Text)
        btn2 = types.InlineKeyboardButton(button2Text)
        btn3 = types.InlineKeyboardButton(button3Text)
        btn4 = types.InlineKeyboardButton(button4Text)
        btn5 = types.InlineKeyboardButton(button5Text)
        btn6 = types.InlineKeyboardButton(button6Text)
        markup.add(btn, btn2, btn3, btn4, btn5, btn6)
        return markup
    elif buttonsCount == 7:
        btn = types.InlineKeyboardButton(button1Text)
        btn2 = types.InlineKeyboardButton(button2Text)
        btn3 = types.InlineKeyboardButton(button3Text)
        btn4 = types.InlineKeyboardButton(button4Text)
        btn5 = types.InlineKeyboardButton(button5Text)
        btn6 = types.InlineKeyboardButton(button6Text)
        btn7 = types.InlineKeyboardButton(button7Text)
        markup.add(btn, btn2, btn3, btn4, btn5, btn6, btn7)
        return markup
    elif buttonsCount == 8:
        btn = types.InlineKeyboardButton(button1Text)
        btn2 = types.InlineKeyboardButton(button2Text)
        btn3 = types.InlineKeyboardButton(button3Text)
        btn4 = types.InlineKeyboardButton(button4Text)
        btn5 = types.InlineKeyboardButton(button5Text)
        btn6 = types.InlineKeyboardButton(button6Text)
        btn7 = types.InlineKeyboardButton(button7Text)
        btn8 = types.InlineKeyboardButton(button8Text)
        markup.add(btn, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        return markup
    elif buttonsCount == 9:
        btn = types.InlineKeyboardButton(button1Text)
        btn2 = types.InlineKeyboardButton(button2Text)
        btn3 = types.InlineKeyboardButton(button3Text)
        btn4 = types.InlineKeyboardButton(button4Text)
        btn5 = types.InlineKeyboardButton(button5Text)
        btn6 = types.InlineKeyboardButton(button6Text)
        btn7 = types.InlineKeyboardButton(button7Text)
        btn8 = types.InlineKeyboardButton(button8Text)
        btn9 = types.InlineKeyboardButton(button9Text)
        markup.add(btn, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        return markup
    else:
        print("Keyboard button error")


# Sends alert signal to get user language
def sendAlertMsg(user_id, user_language):
    if user_language == "ru":
        markup = types.InlineKeyboardMarkup()
        con = types.InlineKeyboardButton(rus_continue_text, callback_data="russian")
        markup.add(con)
        bot.send_message(user_id, rus_press_text, reply_markup=markup)
    elif user_language == "en":
        markup = types.InlineKeyboardMarkup()
        con = types.InlineKeyboardButton(eng_continue_text, callback_data="english")
        markup.add(con)
        bot.send_message(user_id, eng_press_text, reply_markup=markup)
    elif user_language == "uz":
        markup = types.InlineKeyboardMarkup()
        con = types.InlineKeyboardButton(uzb_continue_text, callback_data="uzbek")
        markup.add(con)
        bot.send_message(user_id, uzb_press_text, reply_markup=markup)
    elif user_language == "kz":
        markup = types.InlineKeyboardMarkup()
        con = types.InlineKeyboardButton(kazkh_continue_text, callback_data="kazakh")
        markup.add(con)
        bot.send_message(user_id, kazkh_press_text, reply_markup=markup)
    elif user_language == "tj":
        markup = types.InlineKeyboardMarkup()
        con = types.InlineKeyboardButton(taj_continue_text, callback_data="tajik")
        markup.add(con)
        bot.send_message(user_id, taj_press_text, reply_markup=markup)


# Sends message with buttons to choose language
def chooseLanguage(iden):
    markup = types.InlineKeyboardMarkup()
    eng = types.InlineKeyboardButton('🇬🇧' + eng_text, callback_data="eng")
    ru = types.InlineKeyboardButton('🇷🇺' + rus_text, callback_data="rus")
    uz = types.InlineKeyboardButton("🇺🇿" + uzb_text, callback_data="uzb")
    kz = types.InlineKeyboardButton('🇰🇿' + kaz_text, callback_data="kazh")
    tj = types.InlineKeyboardButton('🇹🇯' + taj_text, callback_data="taj")
    markup.add(eng, ru, uz, kz, tj)
    bot.send_message(iden, choose_lan_text, reply_markup=markup)


# Deletes message of the bot
def deleteMsg(chat_id, mess_id):
    try:
        bot.delete_message(chat_id, mess_id)
    except Exception as e:
        print(f"Error when deleting message: {e}")
        sendErrorToOwner(f"Error when deleting message: {e},chat id {chat_id}")


# Checks language to create subscription buttons
def subscription(user_id, user_language):
    if user_language == "ru":
        create_subscription_buttons(user_id, rus_youtube_channel_sub_text, rus_telegram_channel_sub_text,
                                    rus_channels_text, rus_i_subed_text)
    elif user_language == "en":
        create_subscription_buttons(user_id, eng_youtube_channel_sub_text, eng_telegram_channel_sub_text,
                                    eng_channels_text, eng_i_subed_text)
    elif user_language == "uz":
        create_subscription_buttons(user_id, uzb_youtube_channel_sub_text, uzb_telegram_channel_sub_text,
                                    uzb_channels_text, uzb_i_subed_text)
    elif user_language == "kz":
        create_subscription_buttons(user_id, kazkh_youtube_channel_sub_text, kazkh_telegram_channel_sub_text,
                                    kazkh_channels_text, kazkh_i_subed_text)
    elif user_language == "tj":
        create_subscription_buttons(user_id, taj_youtube_channel_sub_text, taj_telegram_channel_sub_text,
                                    taj_channels_text, taj_i_subed_text)


# Creates subscription buttons
def create_subscription_buttons(user_id, ytbText, tgText, channelsText, iSubText):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(ytbText, url=youTubeChannel)
    button2 = types.InlineKeyboardButton(tgText, url=telegramLink)
    button3 = types.InlineKeyboardButton(iSubText, callback_data="checkSub")
    markup.add(button1, button2, button3)
    bot.send_message(user_id, channelsText, reply_markup=markup)


# Checks language to create subscription buttons
def check_subscription(user_id: int, locale: str, callId):
    if locale == "ru":
        sub(user_id, rus_passed_test_text, rus_failed_test_text, rus_error_test_text, callId)
    elif locale == "en":
        sub(user_id, eng_passed_test_text, eng_failed_test_text, eng_error_test_text, callId)
    elif locale == "uz":
        sub(user_id, uzb_passed_test_text, uzb_failed_test_text, uzb_error_test_text, callId)
    elif locale == "kz":
        sub(user_id, kazkh_passed_test_text, kazkh_failed_test_text, kazkh_error_test_text, callId)
    elif locale == "tj":
        sub(user_id, taj_passed_test_text, taj_failed_test_text, taj_error_test_text, callId)


# Checks subscription of user to needed channel
def sub(user_id: int, passedText, failedText, errorText, callId: int):
    try:
        a = bot.get_chat_member(chat_id=telegramChanel, user_id=user_id)
        if not a.status == 'left':
            bot.answer_callback_query(callback_query_id=callId, text=passedText, show_alert=True)
        else:
            bot.answer_callback_query(callback_query_id=callId, text=failedText, show_alert=True)
    except Exception as e:
        send_message(user_id, errorText)
        print(f"Error when using function sub: {e}")
        sendErrorToOwner(f"Error when function sub: {e},chat id {user_id}")


# Send photo to user
def sendPhoto(chatId, photoSrc):
    try:
        bot.send_chat_action(chatId, "upload_photo")
        bot.send_photo(chatId, photoSrc)
    except Exception as e:
        print(f"Error when sending photo: {e}")
        sendErrorToOwner(f"Error when sending photo: {e},chat id {chatId}")


# Sends more messages using only one function
def sendMoreMessages(chatId, messCount: int = 2, mess1: str = "", mess2: str = "", mess3: str = ""):
    if messCount == 2:
        send_message(chatId, mess1)
        send_message(chatId, mess2)
    elif messCount == 3:
        send_message(chatId, mess1)
        send_message(chatId, mess2)
        send_message(chatId, mess3)
    else:
        print("sendMore messages Error")


# Changes user language
def updateUserLanguage(user_id):
    markup = types.InlineKeyboardMarkup()
    eng = types.InlineKeyboardButton('🇬🇧' + eng_text, callback_data="upd_eng")
    ru = types.InlineKeyboardButton('🇷🇺' + rus_text, callback_data="upd_rus")
    uz = types.InlineKeyboardButton("🇺🇿" + uzb_text, callback_data="upd_uzb")
    kz = types.InlineKeyboardButton('🇰🇿' + kaz_text, callback_data="upd_kazh")
    tj = types.InlineKeyboardButton('🇹🇯' + taj_text, callback_data="upd_taj")
    markup.add(eng, ru, uz, kz, tj)
    bot.send_message(user_id, choose_lan_text, reply_markup=markup)


# Gives admin status to user
def addAdmin(message):
    sender_id = message.chat.id
    id_of_adding_admin = message.text.strip()
    try:
        if id_of_adding_admin == rus_cancel_text:
            pass
        elif id_of_adding_admin == eng_cancel_text:
            pass
        elif id_of_adding_admin == uzb_cancel_text:
            pass
        elif id_of_adding_admin == kazkh_cancel_text:
            pass
        elif id_of_adding_admin == taj_cancel_text:
            pass
        else:
            id_of_adding_admin = int(message.text.strip())
    except ValueError:
        if checkLanguage(sender_id) == "ru":
            sendMakeError(sender_id)
            sendPhoto(sender_id, enterIdPhoto)
            openAdminMenu(sender_id, rus_add_admin_text, rus_delete_admin_text, rus_get_all_users_text,
                          rus_distribution_text, rus_back_text, rus_operation_cancel_text)
        elif checkLanguage(sender_id) == "en":
            sendMakeError(sender_id)
            sendPhoto(sender_id, enterIdPhoto)
            openAdminMenu(sender_id, eng_add_admin_text, eng_delete_admin_text, eng_get_all_users_text,
                          eng_distribution_text, eng_back_text, eng_operation_cancel_text)
        elif checkLanguage(sender_id) == "uz":
            sendMakeError(sender_id)
            sendPhoto(sender_id, enterIdPhoto)
            openAdminMenu(sender_id, uzb_add_admin_text, uzb_delete_admin_text, uzb_get_all_users_text,
                          uzb_distribution_text, uzb_back_text, uzb_operation_cancel_text)
        elif checkLanguage(sender_id) == "kz":
            sendMakeError(sender_id)
            sendPhoto(sender_id, enterIdPhoto)
            openAdminMenu(sender_id, kazkh_add_admin_text, kazkh_delete_admin_text, kazkh_get_all_users_text,
                          kazkh_distribution_text, kazkh_back_text, kazkh_operation_cancel_text)
        elif checkLanguage(sender_id) == "tj":
            sendMakeError(sender_id)
            sendPhoto(sender_id, enterIdPhoto)
            openAdminMenu(sender_id, taj_add_admin_text, taj_delete_admin_text, taj_get_all_users_text,
                          taj_distribution_text, taj_back_text, taj_operation_cancel_text)
        return
    if checkLanguage(sender_id) == "ru":
        if message.text == rus_cancel_text:
            openAdminMenu(sender_id, rus_add_admin_text, rus_delete_admin_text, rus_get_all_users_text,
                          rus_distribution_text, rus_back_text, rus_operation_cancel_text)
        else:
            if updateUserAdmin(id_of_adding_admin, admin_status_text) == success_text:
                openAdminMenu(sender_id, rus_add_admin_text, rus_delete_admin_text, rus_get_all_users_text,
                              rus_distribution_text, rus_back_text, rus_admin_add_succes_text)
            else:
                openAdminMenu(sender_id, rus_add_admin_text, rus_delete_admin_text, rus_get_all_users_text,
                              rus_distribution_text, rus_back_text, rus_admin_add_fail_text)
    elif checkLanguage(sender_id) == "en":
        if message.text == eng_cancel_text:
            openAdminMenu(sender_id, eng_add_admin_text, eng_delete_admin_text, eng_get_all_users_text,
                          eng_distribution_text, eng_back_text, eng_operation_cancel_text)
        else:
            if updateUserAdmin(id_of_adding_admin, admin_status_text) == success_text:
                openAdminMenu(sender_id, eng_add_admin_text, eng_delete_admin_text, eng_get_all_users_text,
                              eng_distribution_text, eng_back_text, eng_admin_add_succes_text)
            else:
                openAdminMenu(sender_id, eng_add_admin_text, eng_delete_admin_text, eng_get_all_users_text,
                              eng_distribution_text, eng_back_text, eng_admin_add_fail_text)
    elif checkLanguage(sender_id) == "uz":
        if message.text == uzb_cancel_text:
            openAdminMenu(sender_id, uzb_add_admin_text, uzb_delete_admin_text, uzb_get_all_users_text,
                          uzb_distribution_text, uzb_back_text, uzb_operation_cancel_text)
        else:
            if updateUserAdmin(id_of_adding_admin, admin_status_text) == success_text:
                openAdminMenu(sender_id, uzb_add_admin_text, uzb_delete_admin_text, uzb_get_all_users_text,
                              uzb_distribution_text, uzb_back_text, uzb_admin_add_succes_text)
            else:
                openAdminMenu(sender_id, uzb_add_admin_text, uzb_delete_admin_text, uzb_get_all_users_text,
                              uzb_distribution_text, uzb_back_text, uzb_admin_add_fail_text)
    elif checkLanguage(sender_id) == "kz":
        if message.text == kazkh_cancel_text:
            openAdminMenu(sender_id, kazkh_add_admin_text, kazkh_delete_admin_text, kazkh_get_all_users_text,
                          kazkh_distribution_text, kazkh_back_text, kazkh_operation_cancel_text)
        else:
            if updateUserAdmin(id_of_adding_admin, admin_status_text) == success_text:
                openAdminMenu(sender_id, kazkh_add_admin_text, kazkh_delete_admin_text, kazkh_get_all_users_text,
                              kazkh_distribution_text, kazkh_back_text, kazkh_admin_add_succes_text)
            else:
                openAdminMenu(sender_id, kazkh_add_admin_text, kazkh_delete_admin_text, kazkh_get_all_users_text,
                              kazkh_distribution_text, kazkh_back_text, kazkh_admin_add_fail_text)
    elif checkLanguage(sender_id) == "tj":
        if message.text == taj_cancel_text:
            openAdminMenu(sender_id, taj_add_admin_text, taj_delete_admin_text, taj_get_all_users_text,
                          taj_distribution_text, taj_back_text, taj_operation_cancel_text)
        else:
            if updateUserAdmin(id_of_adding_admin, admin_status_text) == success_text:
                openAdminMenu(sender_id, taj_add_admin_text, taj_delete_admin_text, taj_get_all_users_text,
                              taj_distribution_text, taj_back_text, taj_admin_add_succes_text)
            else:
                openAdminMenu(sender_id, taj_add_admin_text, taj_delete_admin_text, taj_get_all_users_text,
                              taj_distribution_text, taj_back_text, taj_admin_add_fail_text)


# Gives user status to user
def deleteAdmin(message):
    id_of_removing_admin = message.text.strip()
    sender_id = message.chat.id
    try:
        if id_of_removing_admin == rus_cancel_text:
            pass
        elif id_of_removing_admin == eng_cancel_text:
            pass
        elif id_of_removing_admin == uzb_cancel_text:
            pass
        elif id_of_removing_admin == kazkh_cancel_text:
            pass
        elif id_of_removing_admin == taj_cancel_text:
            pass
        else:
            id_of_removing_admin = int(message.text.strip())
    except ValueError:
        if checkLanguage(sender_id) == "ru":
            sendMakeError(sender_id)
            sendPhoto(sender_id, enterIdPhoto)
            openAdminMenu(sender_id, rus_add_admin_text, rus_delete_admin_text, rus_get_all_users_text,
                          rus_distribution_text, rus_back_text, rus_operation_cancel_text)
        elif checkLanguage(sender_id) == "en":
            sendMakeError(sender_id)
            sendPhoto(sender_id, enterIdPhoto)
            openAdminMenu(sender_id, eng_add_admin_text, eng_delete_admin_text, eng_get_all_users_text,
                          eng_distribution_text, eng_back_text, eng_operation_cancel_text)
        elif checkLanguage(sender_id) == "uz":
            sendMakeError(sender_id)
            sendPhoto(sender_id, enterIdPhoto)
            openAdminMenu(sender_id, uzb_add_admin_text, uzb_delete_admin_text, uzb_get_all_users_text,
                          uzb_distribution_text, uzb_back_text, uzb_operation_cancel_text)
        elif checkLanguage(sender_id) == "kz":
            sendMakeError(sender_id)
            sendPhoto(sender_id, enterIdPhoto)
            openAdminMenu(sender_id, kazkh_add_admin_text, kazkh_delete_admin_text, kazkh_get_all_users_text,
                          kazkh_distribution_text, kazkh_back_text, kazkh_operation_cancel_text)
        elif checkLanguage(sender_id) == "tj":
            sendMakeError(sender_id)
            sendPhoto(sender_id, enterIdPhoto)
            openAdminMenu(sender_id, taj_add_admin_text, taj_delete_admin_text, taj_get_all_users_text,
                          taj_distribution_text, taj_back_text, taj_operation_cancel_text)
        return
    if checkLanguage(sender_id) == "ru":
        if message.text == rus_cancel_text:
            openAdminMenu(sender_id, rus_add_admin_text, rus_delete_admin_text, rus_get_all_users_text,
                          rus_distribution_text, rus_back_text, rus_operation_cancel_text)
        else:
            if updateUserAdmin(id_of_removing_admin, user_text) == success_text:
                openAdminMenu(sender_id, rus_add_admin_text, rus_delete_admin_text, rus_get_all_users_text,
                              rus_distribution_text, rus_back_text, rus_admin_add_succes_text)
            else:
                openAdminMenu(sender_id, rus_add_admin_text, rus_delete_admin_text, rus_get_all_users_text,
                              rus_distribution_text, rus_back_text, rus_admin_add_fail_text)
    elif checkLanguage(sender_id) == "en":
        if message.text == eng_cancel_text:
            openAdminMenu(sender_id, eng_add_admin_text, eng_delete_admin_text, eng_get_all_users_text,
                          eng_distribution_text, eng_back_text, eng_operation_cancel_text)
        else:
            if updateUserAdmin(id_of_removing_admin, user_text) == success_text:
                openAdminMenu(sender_id, eng_add_admin_text, eng_delete_admin_text, eng_get_all_users_text,
                              eng_distribution_text, eng_back_text, eng_admin_add_succes_text)
            else:
                openAdminMenu(sender_id, eng_add_admin_text, eng_delete_admin_text, eng_get_all_users_text,
                              eng_distribution_text, eng_back_text, eng_admin_add_fail_text)
    elif checkLanguage(sender_id) == "uz":
        if message.text == uzb_cancel_text:
            openAdminMenu(sender_id, uzb_add_admin_text, uzb_delete_admin_text, uzb_get_all_users_text,
                          uzb_distribution_text, uzb_back_text, uzb_operation_cancel_text)
        else:
            if updateUserAdmin(id_of_removing_admin, user_text) == success_text:
                openAdminMenu(sender_id, uzb_add_admin_text, uzb_delete_admin_text, uzb_get_all_users_text,
                              uzb_distribution_text, uzb_back_text, uzb_admin_add_succes_text)
            else:
                openAdminMenu(sender_id, uzb_add_admin_text, uzb_delete_admin_text, uzb_get_all_users_text,
                              uzb_distribution_text, uzb_back_text, uzb_admin_add_fail_text)
    elif checkLanguage(sender_id) == "kz":
        if message.text == kazkh_cancel_text:
            openAdminMenu(sender_id, kazkh_add_admin_text, kazkh_delete_admin_text, kazkh_get_all_users_text,
                          kazkh_distribution_text, kazkh_back_text, kazkh_operation_cancel_text)
        else:
            if updateUserAdmin(id_of_removing_admin, user_text) == success_text:
                openAdminMenu(sender_id, kazkh_add_admin_text, kazkh_delete_admin_text, kazkh_get_all_users_text,
                              kazkh_distribution_text, kazkh_back_text, kazkh_admin_add_succes_text)
            else:
                openAdminMenu(sender_id, kazkh_add_admin_text, kazkh_delete_admin_text, kazkh_get_all_users_text,
                              kazkh_distribution_text, kazkh_back_text, kazkh_admin_add_fail_text)
    elif checkLanguage(sender_id) == "tj":
        if message.text == taj_cancel_text:
            openAdminMenu(sender_id, taj_add_admin_text, taj_delete_admin_text, taj_get_all_users_text,
                          taj_distribution_text, taj_back_text, taj_operation_cancel_text)
        else:
            if updateUserAdmin(id_of_removing_admin, user_text) == success_text:
                openAdminMenu(sender_id, taj_add_admin_text, taj_delete_admin_text, taj_get_all_users_text,
                              taj_distribution_text, taj_back_text, taj_admin_add_succes_text)
            else:
                openAdminMenu(sender_id, taj_add_admin_text, taj_delete_admin_text, taj_get_all_users_text,
                              taj_distribution_text, taj_back_text, taj_admin_add_fail_text)


# Makes distribution in bot
def makeDistributionMessage(message):
    mess = message.text
    sender_id = message.chat.id
    if message.text == rus_cancel_text:
        openAdminMenu(sender_id, rus_add_admin_text, rus_delete_admin_text, rus_get_all_users_text,
                      rus_distribution_text, rus_back_text, rus_operation_cancel_text)
    elif message.text == eng_cancel_text:
        openAdminMenu(sender_id, eng_add_admin_text, eng_delete_admin_text, eng_get_all_users_text,
                      eng_distribution_text, eng_back_text, eng_operation_cancel_text)
    elif message.text == uzb_cancel_text:
        openAdminMenu(sender_id, uzb_add_admin_text, uzb_delete_admin_text, uzb_get_all_users_text,
                      uzb_distribution_text, uzb_back_text, uzb_operation_cancel_text)
    elif message.text == kazkh_cancel_text:
        openAdminMenu(sender_id, kazkh_add_admin_text, kazkh_delete_admin_text, kazkh_get_all_users_text,
                      kazkh_distribution_text, kazkh_back_text, kazkh_operation_cancel_text)
    elif message.text == taj_cancel_text:
        openAdminMenu(sender_id, taj_add_admin_text, taj_delete_admin_text, taj_get_all_users_text,
                      taj_distribution_text, taj_back_text, taj_operation_cancel_text)
    else:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        try:
            cursor.execute('SELECT user_id FROM users')
            user_list = cursor.fetchall()
            blockedUser = ""
            try:
                for element in user_list:
                    el = f"{element}"
                    user = el.replace("(", "").replace(")", "").replace(",", "")
                    if checkIsUserBannedOrDeleted(user) == "Clear":
                        blockedUser = user
                        try:
                            send_message(user, mess)
                        except Exception as e:
                            print(f"Error when sending message {user},{e}")
                            sendErrorToOwner(f"{user} banned or cleared chat: {e}")
                            changeUserState(user, "Banned")
                if checkLanguage(sender_id) == "ru":
                    openAdminMenu(sender_id, rus_add_admin_text, rus_delete_admin_text, rus_get_all_users_text,
                                  rus_distribution_text, rus_back_text, rus_send_dist_success_text)
                elif checkLanguage(sender_id) == "en":
                    openAdminMenu(sender_id, eng_add_admin_text, eng_delete_admin_text, eng_get_all_users_text,
                                  eng_distribution_text, eng_back_text, eng_send_dist_success_text)
                elif checkLanguage(sender_id) == "uz":
                    openAdminMenu(sender_id, uzb_add_admin_text, uzb_delete_admin_text, uzb_get_all_users_text,
                                  uzb_distribution_text, uzb_back_text, uzb_send_dist_success_text)
                elif checkLanguage(sender_id) == "kz":
                    openAdminMenu(sender_id, kazkh_add_admin_text, kazkh_delete_admin_text, kazkh_get_all_users_text,
                                  kazkh_distribution_text, kazkh_back_text, kazkh_send_dist_success_text)
                elif checkLanguage(sender_id) == "tj":
                    openAdminMenu(sender_id, taj_add_admin_text, taj_delete_admin_text, taj_get_all_users_text,
                                  taj_distribution_text, taj_back_text, taj_send_dist_success_text)
            except Exception as e:
                print(f'{e}')
                send_message(owner_id, f"Blocked User: {blockedUser} ")
                cursor.close()
                connection.close()
        except Exception as e:
            cursor.close()
            connection.close()
            if checkLanguage(sender_id) == "ru":
                send_message(sender_id, rus_error_test_text)
            elif checkLanguage(sender_id) == "en":
                send_message(sender_id, eng_error_test_text)
            elif checkLanguage(sender_id) == "uz":
                send_message(sender_id, uzb_error_test_text)
            elif checkLanguage(sender_id) == "kz":
                send_message(sender_id, kazkh_error_test_text)
            elif checkLanguage(sender_id) == "tj":
                send_message(sender_id, taj_error_test_text)
            print(f"Error when distribution {e}")
            sendErrorMessToUser(sender_id)
            sendErrorToOwner(f"Error when distribution: {e},chat id {sender_id}")


# Sends apk file to user
def sendApkFile(user_id):
    try:
        bot.send_chat_action(user_id, "upload_document")
        with open(apk_src, "rb") as file:
            f = file.read()

        bot.send_document(user_id, f, visible_file_name="AlanProApp.apk")
    except Exception as e:
        print(f"Error when sending apk: {e}")
        sendErrorMessToUser(user_id)
        sendErrorToOwner(f"Error when sending apk: {e},chat id {user_id}")


# Opens admin settings menu
def openAdminMenu(user_id, btn1Text: str, btn2Text: str, btn3Text: str, btn4Text: str, btn6Text: str,
                  replayedMessText: str):
    buttons = createKeyboardButtons(5, True, 2, btn1Text, btn2Text,
                                    btn3Text, btn4Text,
                                    btn6Text)
    send_button_message(user_id, replayedMessText, buttons)


# Opens admin menu
def openSimpleAdminMenu(user_id, btn1Text: str, btn2Text: str, btn3Text: str, menuText: str):
    butt = createKeyboardButtons(3, True, 2, btn1Text, btn2Text,
                                 btn3Text)
    send_button_message(user_id, menuText, replyMarkup=butt)


# Opens simple main menu
def openSimpleMenu(user_id, btn1Text: str, btn2Text: str, menuText: str):
    butt = createKeyboardButtons(2, True, 2, btn1Text, btn2Text)
    send_button_message(user_id, mess=menuText, replyMarkup=butt)


# Opens InfoMenu
def openInfoMenu(user_id, button1Text,
                 button2Text, button3Text, button4Text, button5Text, button6Text, button7Text, button8Text, button9Text,
                 menuText):
    buttons = createKeyboardButtons(9, True, 2, button1Text, button2Text,
                                    button3Text, button4Text,
                                    button5Text, button6Text, button7Text,
                                    button8Text,
                                    button9Text)
    send_button_message(user_id, menuText, buttons)


def openSecretMenu(txt):
    asd = createKeyboardButtons(6, True, 2, delete_user_text, return_admin_text, send_message_to_user,
                                send_mess_to_group, full_list_users, rus_back_text)
    send_button_message(owner_id, txt, asd)


# Send error message to user
def sendMakeError(user_id):
    if checkLanguage(user_id) == "ru":
        send_message(user_id, rus_value_error_text)
    elif checkLanguage(user_id) == "en":
        send_message(user_id, eng_value_error_text)
    elif checkLanguage(user_id) == "uz":
        send_message(user_id, uzb_value_error_text)
    elif checkLanguage(user_id) == "kz":
        send_message(user_id, kazkh_value_error_text)
    elif checkLanguage(user_id) == "tj":
        send_message(user_id, taj_value_error_text)


# Sends channel photos to user
def sendChannelPhotos(chat_id):
    sendPhoto(chat_id, photo)
    sendPhoto(chat_id, photo_two)
    sendPhoto(chat_id, photo_three)
    sendPhoto(chat_id, photo_four)


# Send error message to user
def sendErrorMessToUser(user_id):
    if checkLanguage(user_id) == "ru":
        send_message(user_id, rus_error_test_text)
    elif checkLanguage(user_id) == "en":
        send_message(user_id, eng_error_test_text)
    elif checkLanguage(user_id) == "uz":
        send_message(user_id, uzb_error_test_text)
    elif checkLanguage(user_id) == "kz":
        send_message(user_id, kazkh_error_test_text)
    elif checkLanguage(user_id) == "tj":
        send_message(user_id, taj_error_test_text)


# Sends message by admin to user
def sendMessageToUserByAdmin(message):
    try:
        sa: str = message.text[:10]
        recipientId = sa.strip()
        messToRecipient = message.text[10:]

        if message.text == rus_cancel_text:
            openSecretMenu(rus_operation_cancel_text)
        else:
            if messToRecipient != "":
                send_message(recipientId, messToRecipient)
                openSecretMenu(send_success_to_user_mess)
            else:
                send_message(owner_id, error_send_message_too)
    except Exception as e:
        print(f"Error when sending message to user: {e}")
        sendErrorToOwner(f"Error when sending message to user: {e}")
        openSecretMenu(rus_error_test_text)


# Sends message to a group
def sendMessageToGroupByAdmin(message):
    try:
        sa: str = message.text[:14]
        recipientId = sa.strip()
        messToRecipient = message.text[14:]

        if message.text == rus_cancel_text:
            openSecretMenu(rus_operation_cancel_text)
        else:
            if messToRecipient != "":
                send_message(recipientId, messToRecipient)
                openSecretMenu(send_success_to_user_mess)
            else:
                send_message(owner_id, error_send_message_too)
    except Exception as e:
        print(f"Error when sending message to user: {e}")
        sendErrorToOwner(f"Error when sending message to user: {e}")
        openSecretMenu(rus_error_test_text)


def sendChannelFriends(chat_id: int, language: str):
    btn = createMoreButtons(2, mocsolay_text, mocsolay_channel_link, kamronPlay_text, kamron_play_channel_link)
    if language == "ru":
        send_button_message(chat_id, rus_friends_text, btn)
    elif language == "en":
        send_button_message(chat_id, eng_friends_text, btn)
    elif language == "uz":
        send_button_message(chat_id, uzb_friends_text, btn)
    elif language == "kz":
        send_button_message(chat_id, kazkh_friends_text, btn)
    elif language == "tj":
        send_button_message(chat_id, taj_friends_text, btn)


######################
# Database functions #
######################


global receiverId


# Saves user to database
def saveUser(user_id, user_name, user_language, user_post, user_tie, user_status, chat_type):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (user_id,user_name,user_tie,user_status,user_language,user_post,chat_type) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (
                    user_id, user_name, user_tie, user_status, user_language, user_post, chat_type))
            connection.commit()
            cursor.close()
            connection.close()
            print(f"User: {user_name} saved!")
            send_message(owner_id, f"User: {user_name},ID: {user_id},UserName: {user_tie} saved!")
        except Exception as e:
            print(f"Error when saving user: {e},chat id {user_id}")
            sendErrorToOwner(f"Error when saving user: {e},chat id {user_id},{user_name},UserName: @{user_tie}")
            sendErrorMessToUser(user_id)
    except Exception as e:
        print(f"Error when connecting to database: {e},chat id {user_id}")
        sendErrorMessToUser(user_id)
        sendErrorToOwner(f"Error when connecting to database: {e},chat id {user_id},{user_name},UserName: @{user_tie}")


# Gets all users from database, and write them to UserList.text file
def getAllUsers():
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users')
        user_list = cursor.fetchall()

        try:
            info = ''
            for element in user_list:
                info += f'{element}'

            with open(user_list_path, "w",
                      encoding="utf-8") as f:
                f.write(f"{user_list}")
            cursor.close()
            connection.close()
        except Exception as e:
            cursor.close()
            connection.close()
            print(f"Error when getting all users {e}")
    except Exception as e:
        print(f"Error when connecting to database and getting all users: {e}")
        sendErrorToOwner(f"Error when connecting to database and getting all users: {e}")


# Gets all users from database, and send them to admin
def getAllUsersToAdmin(user_id, user_language):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users')
        user_list = cursor.fetchall()
        info = ''
        try:
            for element in user_list:
                if element[3] == "Clear":
                    dialog_type = element[6]
                    chat_type = ""
                    post = element[5]
                    mainPost = ""
                    if post == admin_status_text:
                        if user_language == "ru":
                            mainPost = rus_admin_status_text
                        elif user_language == "en":
                            mainPost = eng_admin_status_text
                        elif user_language == "uz":
                            mainPost = uzb_admin_status_text
                        elif user_language == "kz":
                            mainPost = kazkh_admin_status_text
                        elif user_language == "tj":
                            mainPost = taj_admin_status_text
                    elif post == user_text:
                        if user_language == "ru":
                            mainPost = rus_user_status_text
                        elif user_language == "en":
                            mainPost = eng_user_status_text
                        elif user_language == "uz":
                            mainPost = uzb_user_status_text
                        elif user_language == "kz":
                            mainPost = kazkh_user_status_text
                        elif user_language == "tj":
                            mainPost = taj_user_status_text
                    if dialog_type == private_type_text:
                        if user_language == "ru":
                            chat_type = rus_chat_type_text
                        elif user_language == "en":
                            chat_type = eng_chat_type_text
                        elif user_language == "uz":
                            chat_type = uzb_chat_type_text
                        elif user_language == "kz":
                            chat_type = kazkh_chat_type_text
                        elif user_language == "tj":
                            chat_type = taj_chat_type_text
                    elif dialog_type == supergroup_type_text:
                        if user_language == "ru":
                            chat_type = rus_group_type_text
                        elif user_language == "en":
                            chat_type = eng_group_type_text
                        elif user_language == "uz":
                            chat_type = uzb_group_type_text
                        elif user_language == "kz":
                            chat_type = kazkh_group_type_text
                        elif user_language == "tj":
                            chat_type = taj_group_type_text
                    if user_language == "ru":
                        info += f'<b>{rus_name_text}</b> <i>{element[1]}</i>, <b>{rus_post_text}</b> <u>{mainPost}</u>,<b>{rus_type_text}</b> {chat_type},<b>{id_text}</b> <code>{element[0]}</code>;\n'
                    elif user_language == "en":
                        info += f'<b>{eng_name_text}</b> <i>{element[1]}</i>, <b>{eng_post_text}</b> <u>{mainPost}</u>,<b>{eng_type_text}</b> {chat_type},<b>{id_text}</b> <code>{element[0]}</code>;\n'
                    elif user_language == "uz":
                        info += f'<b>{uzb_name_text}</b> <i>{element[1]}</i>, <b>{uzb_post_text}</b> <u>{mainPost}</u>,<b>{uzb_type_text}</b> {chat_type},<b>{id_text}</b> <code>{element[0]}</code>;\n'
                    elif user_language == "kz":
                        info += f'<b>{kazkh_name_text}</b> <i>{element[1]}</i>, <b>{kazkh_post_text}</b> <u>{mainPost}</u>,<b>{kazkh_type_text}</b> {chat_type},<b>{id_text}</b> <code>{element[0]}</code>;\n'
                    elif user_language == "tj":
                        info += f'<b>{taj_name_text}</b> <i>{element[1]}</i>, <b>{taj_post_text}</b> <u>{mainPost}</u>,<b>{taj_type_text}</b> {chat_type},<b>{id_text}</b> <code>{element[0]}</code>;\n'
            send_message(user_id, info, 'html')
            cursor.close()
            connection.close()
        except Exception as e:
            cursor.close()
            connection.close()
            sendErrorMessToUser(user_id)
            print(f"Error when getting all users to admin: {e}")
            sendErrorToOwner(f"Error when getting all users to admin: {e},chat id {user_id}")
    except Exception as e:
        print(f"Error when getting all users to admin,connecting to database: {e}")
        sendErrorMessToUser(user_id)
        sendErrorToOwner(f"Error when getting all users to admin,connecting to database: {e},chat id {user_id}")


# Checks is user registered in bot
def isUserInDb(user_id):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        cursor.execute("SELECT user_id FROM users WHERE user_id='%s'" % user_id)

        res = cursor.fetchone()
        connection.commit()
        cursor.close()
        connection.close()
        if res is None:
            return False
        else:
            changeUserState(user_id, "Clear")
            if checkLanguage(user_id) == "ru":
                sendAlertMsg(user_id, "ru")
            elif checkLanguage(user_id) == "en":
                sendAlertMsg(user_id, "en")
            elif checkLanguage(user_id) == "uz":
                sendAlertMsg(user_id, "uz")
            elif checkLanguage(user_id) == "kz":
                sendAlertMsg(user_id, "kz")
            elif checkLanguage(user_id) == "tj":
                sendAlertMsg(user_id, "tj")
            return True
    except Exception as e:
        print(f"Error when checking user in db: {e}")
        send_message(user_id, global_error_text)
        sendErrorToOwner(f"Error when checking user in db: {e},chat id {user_id}")


# Gets the language of user
def checkLanguage(user_id):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute("SELECT user_language FROM users WHERE user_id = '%s'" % user_id)
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        try:
            info = ''
            for element in user:
                info += f'{element}'
            return info
        except Exception as e:
            print(f"Error when checking language: {e}")
            sendErrorToOwner(f"Error when checking language: {e},chat id {user_id}")
            send_message(user_id, global_error_text)
    except Exception as e:
        print(f"Error when connecting to database and checking language : {e}")
        send_message(user_id, global_error_text)
        sendErrorToOwner(f"Error when connecting to database and checking language: {e},chat id {user_id}")


# Gets status of user
def getStatus(user_id):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute("SELECT user_post FROM users WHERE user_id = '%s'" % user_id)
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        info = ''
        try:
            for element in user:
                info += f'{element}'
            return info
        except Exception as e:
            print(f"Error when getting status: {e}")
            sendErrorToOwner(f"Error when getting status: {e},chat id {user_id}")
            sendErrorMessToUser(user_id)
    except Exception as e:
        print(f"Error when connecting to database and getting status: {e}")
        sendErrorMessToUser(user_id)
        sendErrorToOwner(f"Error when  connecting to database and getting status: {e},chat id {user_id}")


# Update function to admins to add admins
def updateUserAdmin(user_id, user_post):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE users SET user_post = '%s' WHERE user_id = '%s'" % (user_post, user_id))
            connection.commit()
            print("User Updated")
            cursor.close()
            connection.close()
            return "success"
        except Exception as e:
            cursor.close()
            connection.close()
            print(f'Error when updating user Admin : {e}')
            sendErrorMessToUser(user_id)
            return "failure"
    except Exception as e:
        print(f"Error when connecting to database and updating userAdmin: {e}")
        sendErrorMessToUser(user_id)
        sendErrorToOwner(f"Error when connecting to database and updating userAdmin: {e},chat id {user_id}")


# To change language of user by him self
def updateUserSelf(user_id, user_language):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE users SET user_language = '%s' WHERE user_id = '%s'" % (
                    user_language, user_id))
            print("User updated him self")
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            cursor.close()
            connection.close()
            print(f"Error when updating userSelf: {e} {user_id}")
            send_message(user_id, global_error_text)
            sendErrorToOwner(f"Error when updating userSelf: {e},chat id {user_id}")
    except Exception as e:
        print(f"Error when connecting to database and updating userSelf: {e}")
        send_message(user_id, global_error_text)
        sendErrorToOwner(f"Error when connecting to database and updating userSelf: {e},chat id {user_id}")


# Deletes user from database
def deleteUser(user_id):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM users WHERE user_id = '%s' " % user_id)
            print("User deleted")
            connection.commit()
            cursor.close()
            connection.close()
            return "success"
        except Exception as e:
            print(f'error when deleting user: {e}')
            connection.commit()
            cursor.close()
            connection.close()
            sendErrorMessToUser(user_id)
            return "failure"
    except Exception as e:
        print(f"Error when connecting to database and deleting user: {e}")
        sendErrorMessToUser(user_id)
        sendErrorToOwner(f"Error when connecting to database and deleting user: {e},chat id {user_id}")


# Deletes user from database, function for special user
def deleteUserAdmin(message):
    try:
        userId = message.text.strip()
        if message.text == rus_cancel_text:
            openSecretMenu(rus_operation_cancel_text)
        else:
            if deleteUser(userId) == success_text:
                openSecretMenu(suc_delete_user)
            else:
                openSecretMenu(rus_error_test_text)
    except Exception as e:
        print(f"Error when deleting userAdmin: {e}")
        sendErrorToOwner(f"Error when deleting userAdmin: {e}")


# Checks user state in database
def checkIsUserBannedOrDeleted(user_id):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute("SELECT user_status FROM users WHERE user_id = '%s'" % user_id)
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        info = ''
        try:
            for element in user:
                info += f'{element}'
            return info
        except Exception as e:
            print(f"Error when getting banned user: {e}")
            sendErrorToOwner(f"Error when getting banned user: {e},chat id {user_id}")
    except Exception as e:
        print(f"Error when connecting to database and getting banned user: {e}")
        sendErrorToOwner(f"Error when  connecting to database and banned user: {e},chat id {user_id}")


# Changes user state in database
def changeUserState(user_id, user_state):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE users SET user_status = '%s' WHERE user_id = '%s'" % (user_state, user_id))
            connection.commit()
            cursor.close()
            connection.close()
            return "success"
        except Exception as e:
            cursor.close()
            connection.close()
            print(f'Error when updating user to banned : {e}')
            return "failure"
    except Exception as e:
        print(f"Error when connecting to database and updating userAdmin: {e}")
        sendErrorToOwner(f"Error when connecting to database and updating userAdmin: {e},chat id {user_id}")


def getAllUsersToSecretAdmin():
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users')
        user_list = cursor.fetchall()
        cursor.close()
        connection.close()
        info = ''
        try:
            for element in user_list:
                lan = element[4]
                mainLan = ""
                if lan == "ru":
                    mainLan = rus_text
                elif lan == "en":
                    mainLan = eng_text
                elif lan == "uz":
                    mainLan = uzb_text
                elif lan == "kz":
                    mainLan = kaz_text
                elif lan == "tj":
                    mainLan = taj_text
                info += f'{rus_name_text} {element[1]}, {rus_lan_of_user_text} {mainLan},{userName_text}: @{element[2]}, {rus_state_text} {element[3]}, {rus_post_text} {element[5]}, Тип: {element[6]}, {id_text} <code>{element[0]}</code>;\n'
            send_message(owner_id, info, "html")
        except Exception as e:
            cursor.close()
            connection.close()
            print(f"Error when getting all users to admin: {e}")
            sendErrorToOwner(f"Error when getting all users to admin: {e}")
    except Exception as e:
        print(f"Error when getting all users to admin,connecting to database: {e}")
        sendErrorToOwner(f"Error when getting all users to admin,connecting to database: {e}")
