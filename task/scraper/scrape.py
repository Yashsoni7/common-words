import requests
from bs4 import BeautifulSoup
import collections

def find_freq_words(url):
    req = requests.get(url)
    data = req.text
    soup = BeautifulSoup(data,'html.parser')
    f = open('text.txt','w')
    txt = ''
    for i in soup.find_all('p'):
        txt = txt + i.text + ' '

    punctuations = '''!()\-[]{};:'"\,<>./?@#$%^&*_~—©1234567890â`’+-*'''

    text_pure = ''

    for i in txt:
        if i not in punctuations:
            text_pure = text_pure + i.lower()

    words = text_pure.split(' ')

    for i in words:
        if i=='':
            words.remove(i)

    f = open('common-words.txt','r')
    common_words = f.read().split()

    wordlist = []
    for i in filter(lambda w: not w in common_words,words):
        wordlist.append(i)

    freq_words = collections.Counter(wordlist).most_common(10)
    return freq_words