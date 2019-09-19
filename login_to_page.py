import hashlib
from encodings.utf_8 import encode
import requests


# from bs4 import BeautifulSoup
from requests import Request, Session


def main():
    session = requests.Session()
    url = 'https://www.kharkovforum.com/login.php?do=login'

    login = 'Mangal'
    password = hashlib.md5('anager'.encode('utf-8'))

    data = {
        'vb_login_username': 'Mangal',
        'cookieuser': '1',
        'vb_login_password': '',
        's': '',
        'securitytoken': 'guest',
        'do': 'login',
        'vb_login_md5password': password.hexdigest(),
        'vb_login_md5password_utf': password.hexdigest(),

    }

    sess = Session()

    # sess = sess.get(url)
    sess = sess.post(url, data=data)

    # if '>Выход<' in encode(resp.text): print('true')

    # head = sess.headers

    # print(sess.headers)

    # resp = Request('GET', 'https://www.kharkovforum.com/index.php', data=data, headers=head)

    # resp = session.get('https://www.kharkovforum.com/index.php', headers=head)

    print(sess.text)


    # with open('C://Users/Sergungo/Desktop/test.html', 'a') as file:
    #     file.write(str(encode(sess.text)))
    #     file.close()
#
# print(resp.text)


if __name__ == "__main__":
    main()
