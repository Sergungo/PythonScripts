import requests

import re

from bs4 import BeautifulSoup

import csv


def get_html(url):
    resp = requests.get(url)  # response
    return resp.text


def get_all_rows(html):

    soup = BeautifulSoup(html, 'lxml')

    data = []

    trs = soup.find('table').find_all('tr')

    trs.pop(0)

    for tr in trs:

        tds = tr.find_all('td')

        for td in tds:

            if len(td.text.strip()) == 3:
                asx_code = td.text.strip()
                print(asx_code)

            if re.search(r'(\d{2}\/\d{2}\/\d{4})', str(td)):
                date = re.sub("^\s+|\n|\r|\s+$", ' ', td.text.strip())
                print(date)

            match = re.search(r'\">\s+([^?]+?)<br', str(td))
            if match:
                headline = match.group(1)
                print(headline)

            # print(asx_code + ' ' + date + ' ' + headline)

            data.append ({'Asx_code': asx_code, 'Date': date, 'Headline': headline} )

    return data


def write_csv(data):
    with open('asxcodes.csv', 'a') as file:
        writer = csv.writer(file)

        writer.writerow((data['Asx_code'], data['Date'], data['Headline']))

        # print(data['Asx_code'], 'parsed')


def main():

    url = 'https://www.asx.com.au/asx/statistics/prevBusDayAnns.do'

    html = get_html(url)

    data = get_all_rows(html)

    # print(data.values())

    # write_csv(data)


if __name__ == "__main__":
    main()
