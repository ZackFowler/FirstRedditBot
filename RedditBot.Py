# A Reddit bot that posts explanation of xkcd comic strips posted in comments
# The explanation is extracted from http://explainxkcd.com
# Created by Ayush Dwivedi (/u/kindw)
# License: MIT License

from bs4 import BeautifulSoup
from urllib.parse import urlparse

import praw
import time
import re
import requests
import bs4

path = 'c:\\users\\zfowler01\\Documents\\GitHub\\FirstRedditBot\\'
# Location of file where id's of already visited comments are maintained

header = '**Current price of the item:**\n'
footer = '\n*---This data was extracted from [PoeNinja](https://www.poe.ninja) | Bot created by u/kindw | [Source code](https://github.com/aydwi/explainxkcdbot)*'
# Text to be posted along with comic description

def authenticate():

    print('Authenticating...\n')
    reddit = praw.Reddit('PoePriceBot', user_agent= 'PoePriceBot')
    print('Authenticated as {}\n'.format(reddit.user.me()))
    return reddit


def main():
    authenticate()

if __name__ == '__main__':
    main()
