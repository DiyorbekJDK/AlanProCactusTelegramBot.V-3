from domain.functions.functions import *
from data.locale.rus_locale import *
from data.locale.eng_locale import *
from data.locale.uzb_locale import *
from data.locale.kzkh_locale import *
from data.locale.tajik_locale import *
from data.util.links import *

##################################
# Main code file, were bots work #
##################################


bot = telebot.TeleBot(bot_token)


def allCode():
    getAllUsers()

    @bot.message_handler(commands=['start'])
    def start_command(talk):
        getAllUsers()
        if not isUserInDb(talk.chat.id):
            chooseLanguage(talk.chat.id)
            getAllUsers()

    @bot.callback_query_handler(func=lambda call: True)
    def call_back(call):
        talk_id = call.message.chat.id
        userName = call.message.chat.first_name
        if call.data == "eng":
            deleteMsg(talk_id, call.message.message_id)
            saveUser(talk_id, userName, "en", "User", call.message.from_user.username, "Clear")
            sendAlertMsg(talk_id, "en")
        elif call.data == "rus":
            deleteMsg(talk_id, call.message.message_id)
            saveUser(talk_id, userName, "ru", "User", call.message.chat.username, "Clear")
            sendAlertMsg(talk_id, "ru")
        elif call.data == "uzb":
            deleteMsg(talk_id, call.message.message_id)
            saveUser(talk_id, userName, "uz", "User", call.message.from_user.username, "Clear")
            sendAlertMsg(talk_id, "uz")
        elif call.data == "kazh":
            deleteMsg(talk_id, call.message.message_id)
            saveUser(talk_id, userName, "kz", "User", call.message.from_user.username, "Clear")
            sendAlertMsg(talk_id, "kz")
        elif call.data == "taj":
            deleteMsg(talk_id, call.message.message_id)
            saveUser(talk_id, userName, "tj", "User", call.message.from_user.username, "Clear")
            sendAlertMsg(talk_id, "tj")
        elif call.data == "checkSub":
            if checkLanguage(talk_id) == "ru":
                check_subscription(talk_id, "ru", call.id)
            elif checkLanguage(talk_id) == "en":
                check_subscription(talk_id, "en", call.id)
            elif checkLanguage(talk_id) == "uz":
                check_subscription(talk_id, "uz", call.id)
            elif checkLanguage(talk_id) == "kz":
                check_subscription(talk_id, "kz", call.id)
            elif checkLanguage(talk_id) == "tj":
                check_subscription(talk_id, "tj", call.id)
        elif call.data == "russian":
            deleteMsg(talk_id, call.message.message_id)
            message_from_user(call.message)
            send_message(call.message.chat.id, rus_welcome_message, "html")
        elif call.data == "english":
            deleteMsg(talk_id, call.message.message_id)
            message_from_user(call.message)
            send_message(call.message.chat.id, eng_welcome_message, "html")
        elif call.data == "uzbek":
            deleteMsg(talk_id, call.message.message_id)
            message_from_user(call.message)
            send_message(call.message.chat.id, uzb_welcome_message, "html")
        elif call.data == "kazakh":
            deleteMsg(talk_id, call.message.message_id)
            message_from_user(call.message)
            send_message(call.message.chat.id, kazkh_welcome_message, "html")
        elif call.data == "tajik":
            deleteMsg(talk_id, call.message.message_id)
            message_from_user(call.message)
            send_message(call.message.chat.id, taj_welcome_message, "html")
        elif call.data == "upd_rus":
            deleteMsg(talk_id, call.message.message_id)
            updateUserSelf(call.message.chat.id, "ru")
            send_message(call.message.chat.id, rus_language_success, "html")
        elif call.data == "upd_eng":
            deleteMsg(talk_id, call.message.message_id)
            updateUserSelf(call.message.chat.id, "en")
            message_from_user(call.message)
            send_message(call.message.chat.id, eng_language_success, "html")
        elif call.data == "upd_uzb":
            deleteMsg(talk_id, call.message.message_id)
            updateUserSelf(call.message.chat.id, "uz")
            message_from_user(call.message)
            send_message(call.message.chat.id, uzb_language_success, "html")
        elif call.data == "upd_kazh":
            deleteMsg(talk_id, call.message.message_id)
            updateUserSelf(call.message.chat.id, "kz")
            message_from_user(call.message)
            send_message(call.message.chat.id, kazkh_language_success, "html")
        elif call.data == "upd_taj":
            deleteMsg(talk_id, call.message.message_id)
            updateUserSelf(call.message.chat.id, "tj")
            message_from_user(call.message)
            send_message(call.message.chat.id, taj_language_success, "html")

    @bot.message_handler(commands=["menu"])
    def menu(message):
        changeUserState(message.chat.id, "Clear")
        if getStatus(message.chat.id) == admin_status_text:
            if checkLanguage(message.chat.id) == "ru":
                openSimpleAdminMenu(message.chat.id, rus_information_text, rus_channels_text2, rus_admin_settings_text,
                                    rus_menu_text)
            elif checkLanguage(message.chat.id) == "en":
                openSimpleAdminMenu(message.chat.id, eng_information_text, eng_channels_text2, eng_admin_settings_text,
                                    eng_menu_text)
            elif checkLanguage(message.chat.id) == "uz":
                openSimpleAdminMenu(message.chat.id, uzb_information_text, uzb_channels_text2, uzb_admin_settings_text,
                                    uzb_menu_text)
            elif checkLanguage(message.chat.id) == "kz":
                openSimpleAdminMenu(message.chat.id, kazkh_information_text, kazkh_channels_text2,
                                    kazkh_admin_settings_text,
                                    kazkh_menu_text)
            elif checkLanguage(message.chat.id) == "tj":
                openSimpleAdminMenu(message.chat.id, taj_information_text, taj_channels_text2,
                                    taj_admin_settings_text,
                                    taj_menu_text)
        else:
            if checkLanguage(message.chat.id) == "ru":
                openSimpleMenu(message.chat.id, rus_information_text, rus_channels_text2, rus_menu_text)
            elif checkLanguage(message.chat.id) == "en":
                openSimpleMenu(message.chat.id, eng_information_text, eng_channels_text2, eng_menu_text)
            elif checkLanguage(message.chat.id) == "uz":
                openSimpleMenu(message.chat.id, uzb_information_text, uzb_channels_text2, uzb_menu_text)
            elif checkLanguage(message.chat.id) == "kz":
                openSimpleMenu(message.chat.id, kazkh_information_text, kazkh_channels_text2, kazkh_menu_text)
            elif checkLanguage(message.chat.id) == "tj":
                openSimpleMenu(message.chat.id, taj_information_text, taj_channels_text2, taj_menu_text)

    @bot.message_handler(commands=["admin"])
    def admin_settings(message):
        if getStatus(message.chat.id) == "Admin":
            if checkLanguage(message.chat.id) == "ru":
                openAdminMenu(message.chat.id, rus_add_admin_text, rus_delete_admin_text, rus_get_all_users_text,
                              rus_distribution_text, rus_back_text, rus_admin_settings_text2)
            elif checkLanguage(message.chat.id) == "en":
                openAdminMenu(message.chat.id, eng_add_admin_text, eng_delete_admin_text, eng_get_all_users_text,
                              eng_distribution_text, eng_back_text, eng_admin_settings_text2)
            elif checkLanguage(message.chat.id) == "uz":
                openAdminMenu(message.chat.id, uzb_add_admin_text, uzb_delete_admin_text, uzb_get_all_users_text,
                              uzb_distribution_text, uzb_back_text, uzb_admin_settings_text2)
            elif checkLanguage(message.chat.id) == "kz":
                openAdminMenu(message.chat.id, kazkh_add_admin_text, kazkh_delete_admin_text, kazkh_get_all_users_text,
                              kazkh_distribution_text, kazkh_back_text, kazkh_admin_settings_text2)
            elif checkLanguage(message.chat.id) == "tj":
                openAdminMenu(message.chat.id, taj_add_admin_text, taj_delete_admin_text, taj_get_all_users_text,
                              taj_distribution_text, taj_back_text, taj_admin_settings_text2)
        else:
            if checkLanguage(message.chat.id) == "ru":
                send_message(message.chat.id, rus_no_rights_text)
            elif checkLanguage(message.chat.id) == "en":
                send_message(message.chat.id, eng_no_rights_text)
            elif checkLanguage(message.chat.id) == "uz":
                send_message(message.chat.id, uzb_no_rights_text)
            elif checkLanguage(message.chat.id) == "kz":
                send_message(message.chat.id, kazkh_no_rights_text)
            elif checkLanguage(message.chat.id) == "tj":
                send_message(message.chat.id, taj_no_rights_text)

    @bot.message_handler(commands=["channels"])
    def channels(message):
        if checkLanguage(message.chat.id) == "ru":
            subscription(message.chat.id, "ru")
        elif checkLanguage(message.chat.id) == "en":
            subscription(message.chat.id, "en")
        elif checkLanguage(message.chat.id) == "uz":
            subscription(message.chat.id, "uz")
        elif checkLanguage(message.chat.id) == "kz":
            subscription(message.chat.id, "kz")
        elif checkLanguage(message.chat.id) == "tj":
            subscription(message.chat.id, "tj")

    @bot.message_handler(commands=['programmer'])
    def programmer(message):
        if checkLanguage(message.chat.id) == "ru":
            button = createButton(rus_order_bot_text, bot_creator_link)
            send_button_message(message.chat.id, rus_bot_creator_text, button)
        elif checkLanguage(message.chat.id) == "en":
            button = createButton(eng_order_bot_text, bot_creator_link)
            send_button_message(message.chat.id, eng_bot_creator_text, button)
        elif checkLanguage(message.chat.id) == "uz":
            button = createButton(uzb_order_bot_text, bot_creator_link)
            send_button_message(message.chat.id, uzb_bot_creator_text, button)
        elif checkLanguage(message.chat.id) == "kz":
            button = createButton(kazkh_order_bot_text, bot_creator_link)
            send_button_message(message.chat.id, kazkh_bot_creator_text, button)
        elif checkLanguage(message.chat.id) == "tj":
            button = createButton(taj_order_bot_text, bot_creator_link)
            send_button_message(message.chat.id, taj_bot_creator_text, button)

    @bot.message_handler(commands=["language"])
    def language(message):
        updateUserLanguage(message.chat.id)

    @bot.message_handler(commands=["hack"])
    def secret(message):
        if message.chat.id == owner_id:
            openSecretMenu(secret_settings_text)

    @bot.message_handler(commands=['stop'])
    def stop(message):
        if message.chat.id == owner_id:
            bot.stop_bot()

    @bot.message_handler(commands=['data'])
    def data(message):
        send_message(message.chat.id, f"{message}")

    @bot.message_handler()
    def message_from_user(message):
        changeUserState(message.chat.id, "Clear")
        if checkLanguage(message.chat.id) == "ru":
            if message.text == rus_channels_text2:
                channels(message)
            elif message.text == rus_information_text:
                openInfoMenu(message.chat.id, rus_about_channel_text, rus_alan_photos_text, rus_most_viewed_video_text,
                             rus_most_viewed_shorts_text, rus_the_new_video_text, rus_app_text, rus_talk_group_text,
                             rus_channel_friends, rus_back_text, rus_information_text)
            elif message.text == rus_about_channel_text:
                sendMoreMessages(message.chat.id, 2, rus_desc_text, rus_channel_desc_text)
            elif message.text == rus_alan_photos_text:
                try:
                    sendChannelPhotos(message.chat.id)
                except Exception as e:
                    send_message(message.chat.id, rus_error_test_text)
                    print(f'Error when sending photo: {e}')
            elif message.text == rus_most_viewed_video_text:
                sendMoreMessages(message.chat.id, 2, rus_most_viewed_horror_text, popular_video)
            elif message.text == rus_most_viewed_shorts_text:
                sendMoreMessages(message.chat.id, 2, rus_most_viewed_short_text, popular_shorts)
            elif message.text == rus_the_new_video_text:
                sendMoreMessages(message.chat.id, 2, rus_newer_video_text, newVideo)
            elif message.text == rus_app_text:
                sendApkFile(message.chat.id)
                send_message(message.chat.id, rus_app_update_text)
            elif message.text == rus_talk_group_text:
                btn = createButton(rus_group_text, talk_group_link)
                send_button_message(message.chat.id, rus_connect_text, btn)
            elif message.text == rus_channel_friends:
                btn = createButton(mocsolay_text, mocsolay_channel_link)
                send_button_message(message.chat.id, rus_friends_text, btn)
            elif message.text == rus_back_text:
                menu(message)
            # Admin settings
            elif message.text == rus_admin_settings_text and getStatus(message.chat.id) == admin_status_text:
                admin_settings(message)
            elif message.text == rus_get_all_users_text and getStatus(message.chat.id) == admin_status_text:
                getAllUsersToAdmin(message.chat.id, checkLanguage(message.chat.id))
            elif message.text == rus_add_admin_text and getStatus(message.chat.id) == admin_status_text:
                cancel = createKeyboardButtons(1, True, 1, rus_cancel_text)
                send_button_message(message.chat.id, rus_send_id_text, cancel)
                bot.register_next_step_handler(message, addAdmin)
            elif message.text == rus_delete_admin_text and getStatus(message.chat.id) == admin_status_text:
                cancel = createKeyboardButtons(1, True, 1, rus_cancel_text)
                send_button_message(message.chat.id, rus_send_id_delete_admin_text, cancel)
                bot.register_next_step_handler(message, deleteAdmin)
            elif message.text == rus_distribution_text and getStatus(message.chat.id) == admin_status_text:
                cancel = createKeyboardButtons(1, True, 1, rus_cancel_text)
                send_button_message(message.chat.id, rus_send_dist_text, cancel)
                bot.register_next_step_handler(message, makeDistributionMessage)
            elif message.text == rus_cancel_text and getStatus(message.chat.id) == admin_status_text:
                openAdminMenu(message.chat.id, rus_add_admin_text, rus_delete_admin_text, rus_get_all_users_text,
                              rus_distribution_text, rus_back_text, rus_operation_cancel_text)
                # Secret settings
            elif message.text == delete_user_text and message.chat.id == owner_id:
                cancel = createKeyboardButtons(1, True, 1, rus_cancel_text)
                send_button_message(message.chat.id, send_id_delet_user, cancel)
                bot.register_next_step_handler(message, deleteUserAdmin)
            elif message.text == return_admin_text and message.chat.id == owner_id:
                updateUserAdmin(owner_id, admin_status_text)
                send_message(message.chat.id, admin_text)
            elif message.text == send_message_to_user and message.chat.id == owner_id:
                bot.register_next_step_handler(message, sendMessageToUserByAdmin)
                cancel = createKeyboardButtons(1, True, 1, rus_cancel_text)
                send_button_message(message.chat.id, send_id_and_message_me, cancel)
            elif message.text == send_mess_to_group and message.chat.id == owner_id:
                bot.register_next_step_handler(message, sendMessageToGroupByAdmin)
                cancel = createKeyboardButtons(1, True, 1, rus_cancel_text)
                send_button_message(message.chat.id, send_id_of_group_and_message_me, cancel)
            elif message.text == full_list_users and message.chat.id == owner_id:
                getAllUsersToSecretAdmin()
        elif checkLanguage(message.chat.id) == "en":
            if message.text == eng_channels_text2:
                channels(message)
            elif message.text == eng_information_text:
                openInfoMenu(message.chat.id, eng_about_channel_text, eng_alan_photos_text,
                             eng_most_viewed_video_text,
                             eng_most_viewed_shorts_text, eng_the_new_video_text, eng_app_text, eng_talk_group_text,
                             eng_channel_friends, eng_back_text, eng_information_text)
            elif message.text == eng_about_channel_text:
                sendMoreMessages(message.chat.id, 2, eng_desc_text, eng_channel_desc_text)
            elif message.text == eng_alan_photos_text:
                try:
                    sendChannelPhotos(message.chat.id)
                except Exception as e:
                    send_message(message.chat.id, eng_error_test_text)
                    print(f'Error sending photo: {e}')
            elif message.text == eng_most_viewed_video_text:
                sendMoreMessages(message.chat.id, 2, eng_most_viewed_horror_text, popular_video)
            elif message.text == eng_most_viewed_shorts_text:
                sendMoreMessages(message.chat.id, 2, eng_most_viewed_short_text, popular_shorts)
            elif message.text == eng_the_new_video_text:
                sendMoreMessages(message.chat.id, 2, eng_newer_video_text, newVideo)
            elif message.text == eng_app_text:
                sendApkFile(message.chat.id)
                send_message(message.chat.id, eng_app_update_text)
            elif message.text == eng_talk_group_text:
                btn = createButton(eng_group_text, talk_group_link)
                send_button_message(message.chat.id, eng_connect_text, btn)
            elif message.text == eng_channel_friends:
                btn = createButton(mocsolay_text, mocsolay_channel_link)
                send_button_message(message.chat.id, eng_friends_text, btn)
            elif message.text == eng_back_text:
                menu(message)
            # Admin settings
            elif message.text == eng_admin_settings_text and getStatus(message.chat.id) == admin_status_text:
                admin_settings(message)
            elif message.text == eng_get_all_users_text and getStatus(message.chat.id) == admin_status_text:
                getAllUsersToAdmin(message.chat.id, checkLanguage(message.chat.id))
            elif message.text == eng_add_admin_text and getStatus(message.chat.id) == admin_status_text:
                cancel = createKeyboardButtons(1, True, 1, eng_cancel_text)
                send_button_message(message.chat.id, eng_send_id_text, cancel)
                bot.register_next_step_handler(message, addAdmin)
            elif message.text == eng_delete_admin_text and getStatus(message.chat.id) == admin_status_text:
                cancel = createKeyboardButtons(1, True, 1, eng_cancel_text)
                send_button_message(message.chat.id, eng_send_id_delete_admin_text, cancel)
                bot.register_next_step_handler(message, deleteAdmin)
            elif message.text == eng_distribution_text and getStatus(message.chat.id) == admin_status_text:
                cancel = createKeyboardButtons(1, True, 1, eng_cancel_text)
                send_button_message(message.chat.id, eng_send_dist_text, cancel)
                bot.register_next_step_handler(message, makeDistributionMessage)
            elif message.text == eng_cancel_text and getStatus(message.chat.id) == admin_status_text:
                openAdminMenu(message.chat.id, eng_add_admin_text, eng_delete_admin_text, eng_get_all_users_text,
                              eng_distribution_text, eng_back_text, eng_operation_cancel_text)
        elif checkLanguage(message.chat.id) == "uz":
            if message.text == uzb_channels_text2:
                channels(message)
            elif message.text == uzb_information_text:
                openInfoMenu(message.chat.id, uzb_about_channel_text, uzb_alan_photos_text,
                             uzb_most_viewed_video_text,
                             uzb_most_viewed_shorts_text, uzb_the_new_video_text, uzb_app_text, uzb_talk_group_text,
                             uzb_channel_friends, uzb_back_text, uzb_information_text)
            elif message.text == uzb_about_channel_text:
                sendMoreMessages(message.chat.id, 2, uzb_desc_text, uzb_channel_desc_text)
            elif message.text == uzb_alan_photos_text:
                try:
                    sendChannelPhotos(message.chat.id)
                except Exception as e:
                    send_message(message.chat.id, uzb_error_test_text)
                    print(f'Error: {e}')
            elif message.text == uzb_most_viewed_video_text:
                sendMoreMessages(message.chat.id, 2, uzb_most_viewed_horror_text, popular_video)
            elif message.text == uzb_most_viewed_shorts_text:
                sendMoreMessages(message.chat.id, 2, uzb_most_viewed_short_text, popular_shorts)
            elif message.text == uzb_the_new_video_text:
                sendMoreMessages(message.chat.id, 2, uzb_newer_video_text, newVideo)
            elif message.text == uzb_app_text:
                sendApkFile(message.chat.id)
                send_message(message.chat.id, uzb_app_update_text)
            elif message.text == uzb_talk_group_text:
                btn = createButton(uzb_group_text, talk_group_link)
                send_button_message(message.chat.id, uzb_connect_text, btn)
            elif message.text == uzb_channel_friends:
                btn = createButton(mocsolay_text, mocsolay_channel_link)
                send_button_message(message.chat.id, uzb_friends_text, btn)
            elif message.text == uzb_back_text:
                menu(message)
            # Admin settings
            elif message.text == uzb_admin_settings_text and getStatus(message.chat.id) == admin_status_text:
                admin_settings(message)
            elif message.text == uzb_get_all_users_text and getStatus(message.chat.id) == admin_status_text:
                getAllUsersToAdmin(message.chat.id, checkLanguage(message.chat.id))
            elif message.text == uzb_add_admin_text and getStatus(message.chat.id) == admin_status_text:
                cancel = createKeyboardButtons(1, True, 1, uzb_cancel_text)
                send_button_message(message.chat.id, uzb_send_id_text, cancel)
                bot.register_next_step_handler(message, addAdmin)
            elif message.text == uzb_delete_admin_text and getStatus(message.chat.id) == admin_status_text:
                cancel = createKeyboardButtons(1, True, 1, uzb_cancel_text)
                send_button_message(message.chat.id, uzb_send_id_delete_admin_text, cancel)
                bot.register_next_step_handler(message, deleteAdmin)
            elif message.text == uzb_distribution_text and getStatus(message.chat.id) == admin_status_text:
                cancel = createKeyboardButtons(1, True, 1, uzb_cancel_text)
                send_button_message(message.chat.id, uzb_send_dist_text, cancel)
                bot.register_next_step_handler(message, makeDistributionMessage)
            elif message.text == uzb_cancel_text and getStatus(message.chat.id) == admin_status_text:
                openAdminMenu(message.chat.id, uzb_add_admin_text, uzb_delete_admin_text, uzb_get_all_users_text,
                              uzb_distribution_text, uzb_back_text, uzb_operation_cancel_text)
        elif checkLanguage(message.chat.id) == "kz":
            if message.text == kazkh_channels_text2:
                channels(message)
            elif message.text == kazkh_information_text:
                openInfoMenu(message.chat.id, kazkh_about_channel_text, kazkh_alan_photos_text,
                             kazkh_most_viewed_video_text,
                             kazkh_most_viewed_shorts_text, kazkh_the_new_video_text, kazkh_app_text,
                             kazkh_talk_group_text,
                             kazkh_channel_friends, kazkh_back_text, kazkh_information_text)
            elif message.text == kazkh_about_channel_text:
                sendMoreMessages(message.chat.id, 2, kazkh_desc_text, kazkh_channel_desc_text)
            elif message.text == kazkh_alan_photos_text:
                try:
                    sendChannelPhotos(message.chat.id)
                except Exception as e:
                    send_message(message.chat.id, kazkh_error_test_text)
                    print(f'Error: {e}')
            elif message.text == kazkh_most_viewed_video_text:
                sendMoreMessages(message.chat.id, 2, kazkh_most_viewed_horror_text, popular_video)
            elif message.text == kazkh_most_viewed_shorts_text:
                sendMoreMessages(message.chat.id, 2, kazkh_most_viewed_short_text, popular_shorts)
            elif message.text == kazkh_the_new_video_text:
                sendMoreMessages(message.chat.id, 2, kazkh_newer_video_text, newVideo)
            elif message.text == kazkh_app_text:
                sendApkFile(message.chat.id)
                send_message(message.chat.id, kazkh_app_update_text)
            elif message.text == kazkh_talk_group_text:
                btn = createButton(kazkh_group_text, talk_group_link)
                send_button_message(message.chat.id, kazkh_connect_text, btn)
            elif message.text == kazkh_channel_friends:
                btn = createButton(mocsolay_text, mocsolay_channel_link)
                send_button_message(message.chat.id, kazkh_friends_text, btn)
            elif message.text == kazkh_back_text:
                menu(message)
            # Admin settings
            elif message.text == kazkh_admin_settings_text and getStatus(message.chat.id) == admin_status_text:
                admin_settings(message)
            elif message.text == kazkh_get_all_users_text and getStatus(message.chat.id) == admin_status_text:
                getAllUsersToAdmin(message.chat.id, checkLanguage(message.chat.id))
            elif message.text == kazkh_add_admin_text and getStatus(message.chat.id) == admin_status_text:
                cancel = createKeyboardButtons(1, True, 1, kazkh_cancel_text)
                send_button_message(message.chat.id, kazkh_send_id_text, cancel)
                bot.register_next_step_handler(message, addAdmin)
            elif message.text == kazkh_delete_admin_text and getStatus(message.chat.id) == admin_status_text:
                cancel = createKeyboardButtons(1, True, 1, kazkh_cancel_text)
                send_button_message(message.chat.id, kazkh_send_id_delete_admin_text, cancel)
                bot.register_next_step_handler(message, deleteAdmin)
            elif message.text == kazkh_distribution_text and getStatus(message.chat.id) == admin_status_text:
                cancel = createKeyboardButtons(1, True, 1, kazkh_cancel_text)
                send_button_message(message.chat.id, kazkh_send_dist_text, cancel)
                bot.register_next_step_handler(message, makeDistributionMessage)
            elif message.text == kazkh_cancel_text and getStatus(message.chat.id) == admin_status_text:
                openAdminMenu(message.chat.id, kazkh_add_admin_text, kazkh_delete_admin_text, kazkh_get_all_users_text,
                              kazkh_distribution_text, kazkh_back_text, kazkh_operation_cancel_text)
        elif checkLanguage(message.chat.id) == "tj":
            if message.text == taj_channels_text2:
                channels(message)
            elif message.text == taj_information_text:
                openInfoMenu(message.chat.id, taj_about_channel_text, taj_alan_photos_text,
                             taj_most_viewed_video_text,
                             taj_most_viewed_shorts_text, taj_the_new_video_text, taj_app_text,
                             taj_talk_group_text,
                             taj_channel_friends, taj_back_text, taj_information_text)
            elif message.text == taj_about_channel_text:
                sendMoreMessages(message.chat.id, 2, taj_desc_text, taj_channel_desc_text)
            elif message.text == taj_alan_photos_text:
                try:
                    sendChannelPhotos(message.chat.id)
                except Exception as e:
                    send_message(message.chat.id, taj_error_test_text)
                    print(f'Error: {e}')
            elif message.text == taj_most_viewed_video_text:
                sendMoreMessages(message.chat.id, 2, taj_most_viewed_horror_text, popular_video)
            elif message.text == taj_most_viewed_shorts_text:
                sendMoreMessages(message.chat.id, 2, taj_most_viewed_short_text, popular_shorts)
            elif message.text == taj_the_new_video_text:
                sendMoreMessages(message.chat.id, 2, taj_newer_video_text, newVideo)
            elif message.text == taj_app_text:
                sendApkFile(message.chat.id)
                send_message(message.chat.id, taj_app_update_text)
            elif message.text == taj_talk_group_text:
                btn = createButton(taj_group_text, talk_group_link)
                send_button_message(message.chat.id, taj_connect_text, btn)
            elif message.text == taj_channel_friends:
                btn = createButton(mocsolay_text, mocsolay_channel_link)
                send_button_message(message.chat.id, taj_friends_text, btn)
            elif message.text == taj_back_text:
                menu(message)
            # Admin settings
            elif message.text == taj_admin_settings_text and getStatus(message.chat.id) == admin_status_text:
                admin_settings(message)
            elif message.text == taj_get_all_users_text and getStatus(message.chat.id) == admin_status_text:
                getAllUsersToAdmin(message.chat.id, checkLanguage(message.chat.id))
            elif message.text == taj_add_admin_text and getStatus(message.chat.id) == admin_status_text:
                cancel = createKeyboardButtons(1, True, 1, taj_cancel_text)
                send_button_message(message.chat.id, taj_send_id_text, cancel)
                bot.register_next_step_handler(message, addAdmin)
            elif message.text == taj_delete_admin_text and getStatus(message.chat.id) == admin_status_text:
                cancel = createKeyboardButtons(1, True, 1, taj_cancel_text)
                send_button_message(message.chat.id, taj_send_id_delete_admin_text, cancel)
                bot.register_next_step_handler(message, deleteAdmin)
            elif message.text == taj_distribution_text and getStatus(message.chat.id) == admin_status_text:
                cancel = createKeyboardButtons(1, True, 1, taj_cancel_text)
                send_button_message(message.chat.id, taj_send_dist_text, cancel)
                bot.register_next_step_handler(message, makeDistributionMessage)
            elif message.text == taj_cancel_text and getStatus(message.chat.id) == admin_status_text:
                openAdminMenu(message.chat.id, taj_add_admin_text, taj_delete_admin_text, taj_get_all_users_text,
                              taj_distribution_text, taj_back_text, taj_operation_cancel_text)

    bot.polling(none_stop=True)
