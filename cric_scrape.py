__author__ = "Harsh"
import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    pages = 1
    while pages <= max_pages:
        url = ("http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;orderby=player;page="
              + str(pages)
              + ";template=results;type=batting")

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.findAll('a', {'class', 'data-link'}):

            href = "http://stats.espncricinfo.com" + link.get('href') + "?class=2;template=results;type=batting"
            href = href.replace("content", "engine")
            print(href)
            print(link.string)
            get_score_data(href)
        pages += 1

def get_score_data(year_url):
    source_code = requests.get(year_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    cum=[]
    for runs in soup.findAll('tr', {'class' : 'data1'}):
        runs_list = runs.text.split('\n')
        if (runs_list[1].find("year") != -1):
            runs_list = [x for x in runs_list if x]

            if(runs_list[4] != '-'):
                cum.append(int(runs_list[4]))
            print(runs_list[0] + ": " + runs_list[4] + ", Cummulative Score: " + str(sum(cum)))

trade_spider(51)

