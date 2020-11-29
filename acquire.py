import pandas as pd

from requests import get
from bs4 import BeautifulSoup
import os

def get_news_articles():
    articles = ['https://inshorts.com/en/news/scientist-behind-90-effective-covid19-vaccine-says-it-can-end-the-pandemic-1605240935577', 'https://inshorts.com/en/news/ipl-is-ready-for-expansion-nca-head-rahul-dravid-1605277577935', 'https://inshorts.com/en/news/something-bogus-going-on-musk-on-2-+ve-2-ve-covid19-results-1605255417135', 'https://inshorts.com/en/news/friends-reunion-being-rescheduled-for-beginning-of-march-perry-1605267450576']

    final = [] 
    i = 0
    for ele in articles:
        cat = ['Business','Sports','Technology','Entertainment']
        url = ele
        headers = {'User-Agent': 'Codeup Data Science Darden Cohort'} # Some websites don't accept the pyhon-requests default user-agent
        response = get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        article_title = soup.title.string
        article = soup.find('div', itemprop='articleBody')
        article_text = article.text
        
        item = {
            'title': article_title,
            'content': article_text,
            'category': cat[i]
        }
        final.append(item)
        i += 1
        with open('article.text', 'w') as f:
            f.write('article_text')
    
    return final

def get_blog_articles():
    urls = ['https://codeup.com/codeups-data-science-career-accelerator-is-here/', 'https://codeup.com/data-science-myths/', 'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/', 'https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/','https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/']

    final = [] 
    for ele in urls:
        url = ele
        headers = {'User-Agent': 'Codeup Data Science'} # Some websites don't accept the pyhon-requests default user-agent
        response = get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        article_title = soup.title.string
        article = soup.find('div', class_='jupiterx-post-content')
        article_text = article.text
        item = {
            'title': article_title,
            'content': article_text
        }
        final.append(item)
    return final