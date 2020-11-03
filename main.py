#!/usr/bin/env python3
"""
Purpose to export a csv of search from my favourite bike sales websites to help me track prices.
"""

__author__ = "Etienne Munnich"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import requests
from bs4 import BeautifulSoup
import random

#Need to send a useragent as the search won't return a result otherwise
user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

def main(args):
    """ Main entry point of the app """
    
    #search offset, used by search page querysting to return the next page, offset is 12 per page
    offset = 0
    for pagecounter in range(int(args.pages)):
        offset = pagecounter * int(args.pages)
        URL = 'https://www.bikesales.com.au/bikes/road/bmw/?offset='+str(offset)
        
        #Pick a random user agent
        user_agent = random.choice(user_agent_list)
        #Set the headers 
        headers = {'User-Agent': user_agent}
        #get the page
        page = requests.get(URL, headers=headers)
        
        #parse
        soup = BeautifulSoup(page.content, 'html.parser')
        
        #find elements
        results = soup.find(class_='listing-items')
        #works advert_elems = results.find_all(class_='card-body')
        advert_elems = results.find_all('div', attrs={"data-webm-searchlist": "results"})

        #Iterate from elemnts and put into comma seperated
        for a in advert_elems:
            title_elem = a.find('a', attrs={"data-webm-clickvalue": "sv-title"}) 
            price_elem = a.find('a', attrs={"data-webm-clickvalue": "sv-price"})
            location_elem = a.find('div', class_='seller-location d-flex')
            typeseller_elem = a.find('div', class_='seller-type')
            if None in (title_elem, price_elem, location_elem, typeseller_elem):
                continue
            print("'"+title_elem.text.strip()[0:4]+"','"+title_elem.text.strip()[5:]+"','"+price_elem.text.strip()[:-1]+"','"+location_elem.text.strip()+"','"+typeseller_elem.text.strip()+"'")

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Optional pages to download 
    parser.add_argument(
        "-p",
        "--pages",
        action="store",
        default=1,
        help="12 items a page, choose the number of pages.")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
