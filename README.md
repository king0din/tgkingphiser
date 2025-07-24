# Telegram Phishing Botu ve Flask Paneli

Bu proje, Telegram üzerinden phishing saldırıları düzenlemek için kullanılan bir bot ve bu botun topladığı bilgileri yönetmek için bir Flask panelinden oluşmaktadır.

## Özellikler

**Telegram Botu:**
- Kullanıcılara farklı sosyal medya platformları (Instagram, Facebook, TikTok) için phishing linkleri sunar.
- Kullanıcıların seçimine göre özel linkler oluşturur.
- Yakında Twitter, Snapchat ve Gmail için de destek eklenecektir.

**Flask Paneli:**
- Phishing linkleri üzerinden toplanan kullanıcı adı, şifre ve IP bilgilerini kaydeder.
- IP adreslerinin detaylı bilgilerini (ülke, şehir, ISP vb.) sorgular.
- Toplanan bilgileri Telegram botuna ve belirlenen bir log grubuna gönderir.

## Kurulum

### Gereksinimler

- Python 3.x
- `pyTelegramBotAPI` kütüphanesi (Telegram botu için)
- `Flask`, `requests`, `beautifulsoup4` kütüphaneleri (Flask paneli için)

### Adımlar

1. **Telegram Bot Tokenı ve Log Grup ID'si:**
   - Telegram'dan yeni bir bot oluşturun ve bot tokenınızı alın.
   - Log bilgilerini göndermek istediğiniz Telegram grubunun ID'sini alın.

2. **`telegram_bot.py` dosyasını düzenleyin:**
   - `BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'` kısmını kendi bot tokenınızla değiştirin.

3. **`flask_app.py` dosyasını düzenleyin:**
   - `TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'` kısmını kendi bot tokenınızla değiştirin.
   - `LOG_GROUP_CHAT_ID = 'YOUR_LOG_GROUP_CHAT_ID_HERE'` kısmını log grup ID'nizle değiştirin.

4. **Bağımlılıkları yükleyin:**

   ```bash
   pip install -r requirements.txt
   pip install pyTelegramBotAPI
   ```

5. **Uygulamaları çalıştırın:**

   ```bash
   python3 flask_app.py
   python3 telegram_bot.py
   ```

   Flask uygulaması `http://0.0.0.0:8080` adresinde çalışacaktır. Botunuzu çalıştırmak için `telegram_bot.py` dosyasını da çalıştırmanız gerekmektedir.

## Kullanım

Telegram botunuzda `/phis` komutunu kullanarak phishing linklerini oluşturabilirsiniz. Kullanıcılar bu linklere tıkladığında, Flask paneli üzerinden giriş bilgileri toplanacak ve size iletilecektir.

## Uyarı

Bu proje yalnızca eğitim ve güvenlik araştırmaları amaçlıdır. Yasa dışı veya kötü niyetli amaçlar için kullanılması kesinlikle yasaktır. Projenin kötüye kullanımından doğacak sonuçlardan geliştirici sorumlu değildir.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.


