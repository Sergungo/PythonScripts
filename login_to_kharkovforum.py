import hashlib
import requests

def main():
    login_url = 'https://www.kharkovforum.com/login.php?do=login'
    main_url = 'https://www.kharkovforum.com/subscription.php'
    login = 'Mangal'
    password = hashlib.md5('anager'.encode('utf-8'))

    session = requests.Session()

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "DNT": "1",
        "Host": "www.kharkovforum.com",
        "Origin": "https://www.kharkovforum.com",
        "Referer": "https://www.kharkovforum.com/index.php",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

    data = {
        'vb_login_username': login,
        'cookieuser': '1',
        'vb_login_password': '',
        's': '',
        'securitytoken': 'guest',
        'do': 'login',
        'vb_login_md5password': password.hexdigest(),
        'vb_login_md5password_utf': password.hexdigest(),

    }

    r1 = session.post(login_url, data=data, headers=headers)
    r2 = session.get(main_url)

    print(r1.url)
    print(r2.url)
    print(r2.text)

    # with open('C://Users/Sergungo/Desktop/test.html', 'a') as file:
    #     file.write(r2.text)
    #     file.close()

if __name__ == "__main__":
    main()
