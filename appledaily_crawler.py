import requests
from bs4 import BeautifulSoup
import re
import csv


DOMAIN = "http://www.appledaily.com.tw"
f = open('./data.csv', 'w')
headers = ['title', 'time', 'content', 'hot']
writer = csv.DictWriter(f, fieldnames=headers)
writer.writeheader()


def list_crawler(page):
    for i in range(1, page + 1):
        rep = requests.get("http://www.appledaily.com.tw/realtimenews/section/new/%s" % i)
        path_list = re.findall('a href="(/realtimenews/article/.*/.*/.*/.+)" target', rep.text)
        url_list = []
        for path in path_list:
            url_list.append(DOMAIN + path)
    article_crawler(url_list)

def article_crawler(url_list):
    for url in url_list:
        rep = requests.get(url)
        soup = BeautifulSoup(rep.text, "html5lib")
        article = {}
        article["title"] = soup.select("#h1")[0].text.strip()
        article["time"] = soup.select("div.gggs > time")[0].text.strip()
        article["content"] = soup.select("#summary")[0].text.strip()
        if soup.select("div.urcc > a.function_icon forward"):
            article["hot"] = int(re.findall("\d+", soup.select("div.urcc > a.function_icon forward")[0].text.strip())[0])
        else:
            article["hot"] = 0

        writer.writerow(article)
        f.flush()


if __name__=="__main__":
    list_crawler(3)