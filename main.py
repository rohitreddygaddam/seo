from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from pylinkvalidator.api import crawl
from seoanalyzer import analyze

url = input("Enter your URL here ")
keyword = input("Enter your keyword you want to check ")
keyword = keyword.casefold()
sitemap = url + '/sitemap.xml'

try:
    html = urlopen(url)
except HTTPError as e:
    print(e)

data = BeautifulSoup(html, "html.parser")


def seo_title_found(keyword, data):
    if data.title:
        if keyword in data.title.text.casefold():
            status = "Keyword found"
        else:
            status = "Keyword Not Found"
    else:
        status = "No title found"
    return status


def seo_title_stop_words(data):
    words = 0
    list_words = []
    if data.title:
        with open('stopwords.txt', 'r') as f:
            for line in f:
                if re.search(r'\b' + line.strip('\n') + r'\b', data.title.text.casefold()):
                    words += 1
                    list_words.append(line.rstrip('\n'))
        if words > 0:
            stop_words = "We found {} stop words in your title. You should consider removing them. {}"\
                .format(words, list_words)
        else:
            stop_words = "We found no stop words in your title. Good work"
    else:
        stop_words = "We could not find any stop words"
    return stop_words


def validate_links(url):
    crawled_site = crawl(url)
    return crawled_site


def seo_analyser(url, sitemap):
    output = analyze(url, sitemap)
    print(output)


print(seo_title_found(keyword, data))
print(seo_title_stop_words(data))
# print(seo_analyser(url, sitemap))
