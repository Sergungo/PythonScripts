import requests

import re

from bs4 import BeautifulSoup

import csv


def get_html(url):
    resp = requests.get(url)  # response
    return resp.text


def get_all_rows(html):

    soup = BeautifulSoup(html, 'lxml')
    # trs = soup.find('table').find_all('tr')

    trs = soup.find('table').find_all('tr')

    rows = []

    print(len(trs))

    for tr in trs:

        tds = tr.find_all('td')
        # print(len(tds))

        try:
            while len(tds) > 0:
                asx_code = tds[0].text.strip()
                print(asx_code)
                date = tds[1].text.strip()
                print(date)         
                # print(tds[3])
                match = re.search(r'">\s+([^?]+?)<br', tds[3])
                if match:
                    print(headline.group(0))
        except:
            axc_code = ''

    # data = {'asx_code': asx_code, 'price': price}

    return rows


# def get_page_data(html):
#     soup = BeautifulSoup(html, 'lxml')

#     try:
#         asc_codes = soup.find('table').find_all('tr', class_='altrow')  #.find('td').text.strip()


#         print(asc_codes)

#     except:
#         asc_code = ''

    # try:
    #     date = soup.find('table').find('tr', class_='').find('td').text.strip()
    #     # print(date)

    # except:
    #     date = ''

    # data = {'AXC CODE': asc_code}  #, 'Date': date
    # return data

# def write_csv(data):
#     with open('coinmarketcap.csv', 'a') as file:
#         writer = csv.writer(file)

#         writer.writerow((data['name'], data['price']))

#         print(data['name'], 'parsed')

def main():

    url = 'https://www.asx.com.au/asx/statistics/prevBusDayAnns.do'

    html = get_html(url)

    data = get_all_rows(html)


if __name__ == "__main__":
    main()
