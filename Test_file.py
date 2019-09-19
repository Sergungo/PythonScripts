import requests


def get_html(url):
    resp = requests.get(url)  # response
    return resp.text


def main():
    url = 'https://www.kharkovforum.com/login.php?do=login'
    resp = get_html(url)
    print(resp)

if __name__ == "__main__":
    main()