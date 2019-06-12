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

    rows = soup.select('table > tr')

    for row in rows:
        cols = row.select('td')

        if len(cols) > 0:
            data.append({
                'ASX': cols[0].text,
                'Date': re.sub("^\s+|\n|\r|\s+$", ' ', cols[1].text).strip(),
                'Headline': re.sub("\n|\r|\t", '', re.search(r'\">([^?]+?)<br', str(cols[3])).group(1)),
            })

    return data


def write_csv(data):
    with open('asxcodes.csv', 'a') as file:
        writer = csv.writer(file)

        writer.writerow(('ASX', 'Date', 'Headline'))

        for dat in data:
            if dat['Headline'] in ("Daily share buy-back notice - Appendix 3E", "Appendix 3e", "Daily share buy-back notice", "nnouncement of  buy-back"):
                writer.writerow((dat['ASX'], dat['Date'], dat['Headline']))
                print(data['ASX'], 'parsed')


def main():

    url = 'https://www.asx.com.au/asx/statistics/prevBusDayAnns.do'

    html = get_html(url)

    data = get_all_rows(html)

    write_csv(data)


if __name__ == "__main__":
    main()
