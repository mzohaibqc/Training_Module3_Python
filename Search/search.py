""" Search Headlines from web
"""
import urllib3

from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz


def search():
    """ Search Headlines from web
    """
    http = urllib3.PoolManager()
    reddit = http.request('GET', 'http://reddit.com/r/programming')
    ycombinator = http.request('GET', 'https://news.ycombinator.com/')
    reddit_soup = BeautifulSoup(reddit.data)
    ycombinator_soup = BeautifulSoup(ycombinator.data)
    while True:
        words = raw_input('Search : ')
        count1 = 0
        count2 = 0
        print('Headings from http://www.reddit.com/r/programming')
        print('=================================================')
        for link in reddit_soup.find_all('a', {'class': "title"}):
            if words in link.text.lower():
                print('     {}'.format(link.text))
                count1 += 1
            elif fuzz.token_set_ratio(words, link.text) > 50:
                print('     {}'.format(link.text))
                count1 += 1
            elif fuzz.ratio(words, link.text) > 50:
                print('     {}'.format(link.text))
                count1 += 1
        if count1 == 0:
            print('No heading found ')
        print('Headings from https://news.ycombinator.com/')
        print('===========================================')
        for line in ycombinator_soup.find_all('td', {'class': "title"}):
            a = line.find('a')
            if a is not None:
                if words in a.string.lower():
                    print('     {}'.format(a.string))
                    count2 += 1
                elif fuzz.token_set_ratio(words, a.string) > 50:
                    print('     {}'.format(a.string))
                    count2 += 1
                elif fuzz.ratio(words, a.string) > 50:
                    print('     {}'.format(a.string))
                    count2 += 1
        if count2 == 0:
            print('No heading found ')


if __name__ == '__main__':
    search()