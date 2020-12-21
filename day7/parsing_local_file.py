import requests

from bs4 import BeautifulSoup
import csv

file_name = 'jokbal.csv'
file = open(file_name, mode="w", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(['title', 'location', 'work_time', 'payment', 'regDate'])

# print(url)
# print(name)
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')
# f = open("eng.html")      # simplified for the example (no urllib)
# f = open("jokbal.html", encoding='utf8')      # simplified for the example (no urllib)
# f = open("/home/jeonghn/dev/python/scraping-challenge/day7/jokbal.html",'rb')
# soup = BeautifulSoup(f)
# f.close()

# with open("/home/jeonghn/dev/python/scraping-challenge/day7/jokbal.html", encoding="utf8") as f:
#     contents = f.read()
#     soup = BeautifulSoup(contents, "html.parser")
# soup=BeautifulSoup(open("/home/jeonghn/dev/python/scraping-challenge/day7/jokbal.html"))
soup=BeautifulSoup(open("/home/jeonghn/dev/python/scraping-challenge/day7/jokbal.html",'rb',encoding='utf8'),'html.parser')
lists = soup.find('div', {"class": "goodsList"})
table = lists.find('tbody')
jobs = table.find_all("tr", {"class": ["divide", ""]})
# trs=table.find_all("tr")
# result = [tr for tr in trs if 'summaryView' not in tr['class']]
# print(jobs[:1])

job_list = []
for job in jobs[:]:
    # print(job)
    job_detail = job.find_all('td')
    # print(job_detail[0].text)
    # print(job_detail[1].find('a').find('span', {"class":"company"}).text)
    # # print(job_detail[1].find('a').find_all('span').select('.company'))
    # print(job_detail[2].find('span',{"class":"time"}).text)
    # print(job_detail[3].find('span', {"class":'payIcon'}).text)
    # print(job_detail[3].find('span', {"class": 'number'}).text)
    # print(job_detail[4].text)
    if job_detail is not None:
        job = {'title': job_detail[1].find('a').find('span', {"class": "company"}).text,
               'location': job_detail[0].text, 'work_time': job_detail[2].find('span', {"class": "time"}).text,
               'payment': job_detail[3].find('span', {"class": 'payIcon'}).text + job_detail[3].find('span', {
                   "class": 'number'}).text, 'regDate': job_detail[4].text}
        # print(job.values)
        # print([job['title'],job['location']])
        writer.writerow([job['title'], job['location'], job['work_time'], job['payment'], job['regDate']])
    else:
        writer.writerow('No available jobs')

file.close()
#
# for job in jobs[:2]: