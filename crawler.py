import requests

from bs4 import BeautifulSoup

import csv

from datetime import datetime


def get_html(url):
    resp = requests.get(url)  # response
    return resp.text


def get_all_links(html):

    soup = BeautifulSoup(html, 'lxml')
    tds = soup.find('table', id='currencies-all').find_all('td',
                                                           class_='currency-name')
    links = []
    for td in tds:
        a = td.find('a', class_='currency-name-container').get('href')
        link = 'https://coinmarketcap.com' + a
        links.append(link)

    return links


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    try:
        name = soup.find('h1', class_='text-large').text.strip()
    except:
        name = ''

        try:
            price = soup.find('span', id='quote-price').text.strip()
        except:
            price = ''

    data = {'name': name, 'price': price}
    return data


def write_csv(data):
    with open('coinmarketcap.csv', 'a') as file:
        writer = csv.writer(file)

        writer.writerow((data['name'], data['price']))

        print(data['name'], 'parsed')


def main():
    start = datetime.now()

    url = 'https://coinmarketcap.com/all/views/all/'

    all_links = get_all_links(get_html(url))

    for link in enumerate(all_links):
        html = get_html(link)
        data = get_page_data(html)
        write_csv(data)

    end = datetime.now()

    total = end - start
    print(str(total))


if __name__ == "__main__":
    main()
