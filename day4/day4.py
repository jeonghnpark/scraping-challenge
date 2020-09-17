import requests
import os
import numpy as np

q_continue=True

def cleanUrls(urls):
    urls = [x for y in [x.split(',') for x in urls.strip().split(' ')] for x in y]
    while ("" in urls):
        urls.remove("")
    for i,url in enumerate(urls):
        if(url[:4]!="http"):
            urls[i]="http://"+url
    return urls

def checkUrl(url):
    # try:
    try:
        html=requests.get(url)
        rs=html.raise_for_status()
        if rs is None:
            return True
        else:
            return False

    except requests.exceptions.RequestException as e:
        return False

while(q_continue==True):
    # os.system('cls')
    print("Welcome to InItDown.py!")
    print("Please write a URL or URLs you want to check. (separated by comma)")
    urls=input()
    urls=cleanUrls(urls)

    for url in urls:
        if('.' not in url):
            print("invalid url ! ")
            continue
        if(checkUrl(url)):
            print(f"{url} is good")
        else:
            print(f"{url} is down")

    y_or_no=""
    while (1) :
        y_or_no=input('Do you want to start over? (y/n)   ')
        if(y_or_no=='y'):
            q_continue=True
            break
        elif(y_or_no=='n'):
            print('ok. bye')
            q_continue=False
            break
        else:
            print("invalid answer ! ")

