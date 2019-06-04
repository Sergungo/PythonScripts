import requests

from bs4 import BeautifulSoup

import csv


def get_html(url):
    resp = requests.get(url)  # response
    return resp.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    try:
        asc_code = soup.find('table').find('tr', class_='altrow').find('td').text.strip()
        
        
        print(asc_code)

    except:
        asc_code = ''

    # try:
    #     date = soup.find('table').find('tr', class_='').find('td').text.strip()
    #     print(asc_code)

    # except:
    #     date = ''

    data = {'AXC CODE': asc_code}  #, 'Date': date
    return data


def main():

    url = 'https://www.asx.com.au/asx/statistics/prevBusDayAnns.do'

    html = get_html(url)

    get_page_data(html)


if __name__ == "__main__":
    main()
