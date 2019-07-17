import requests
from bs4 import BeautifulSoup
import re
import argparse


def scrape(url):
    r = requests.get(url)

    content = BeautifulSoup(r.text, 'html.parser')

    #CLASS EXTRACTION
    priceClass = content.find(class_ = '_1vC4OE _3qQ9m1')
    ratingClass = content.find(class_ = '_1i0wk8')
    vfmClass = content.find(class_ = 'PRNS4f')
    warrantyClass = content.find(class_ = '_3h7IGd')

    #VALUE EXTRACTION
    price = re.sub('[^0-9]', '', priceClass.contents[0])
    rating = re.sub('[^0-9\.]', '', ratingClass.contents[0])
    vfm = re.sub('[^0-9\.]', '', vfmClass.contents[0])
    war = warrantyClass.contents[0].split()
    for i in range(len(war)):
        if war[i].isnumeric():
            if war[i + 1] == 'Year':
                warranty = int(war[i]) * 12
            else:
                warranty = int(war[i])
            break

    #OUTPUT: PRICE, TOTAL RATING, VALUE FOR MONEY RATING, WARRANTY IN YEARS
    return (price, rating, vfm, warranty)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Flipkart Value Scraper')
    parser.add_argument('url', type = str, help = 'Flipkart product link')
    args = parser.parse_args()

    scrape(args.url.split('?')[0])
