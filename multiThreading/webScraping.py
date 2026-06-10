''''
Real-World Example: Multithreading for I/O-bound Tasks

Scenario: Web Scraping

Web scraping often involves making numerous network requests to
fetch web pages. These tasks are I/O-bound because they spend a lot of
time waiting for responses from servers. Multithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently.

'''
'''
https://docs.langchain.com/langsmith/engine
https://docs.langchain.com/langsmith/prompt-engineering
https://docs.langchain.com/langsmith/observability

'''

import threading
import requests
from bs4 import BeautifulSoup
urls=[
'https://docs.langchain.com/langsmith/engine',
'https://docs.langchain.com/langsmith/prompt-engineering',
'https://docs.langchain.com/langsmith/observability'
]

def fetch_content(url):
    response = requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'{len(soup.text)} charachters from {url}')

threads = [] 
for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

print("Done")