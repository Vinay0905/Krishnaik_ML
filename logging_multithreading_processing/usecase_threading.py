# '''
# https://docs.langchain.com/oss/python/langchain/guardrails

# https://docs.langchain.com/oss/python/langchain/runtime

# https://docs.langchain.com/oss/python/langchain/human-in-the-loop

# '''


import threading
import requests
import time
from  bs4  import BeautifulSoup


urls=[

    'https://docs.langchain.com/oss/python/langchain/guardrails',

    'https://docs.langchain.com/oss/python/langchain/runtime',

    'https://docs.langchain.com/oss/python/langchain/human-in-the-loop'

]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')

    print(f"Fetched  {len(soup.text)} characters from {url}")



threads=[]


for url in urls :
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


print("All web pages fetched successfully")


