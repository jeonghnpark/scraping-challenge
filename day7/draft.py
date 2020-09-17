import csv

import requests
from bs4 import BeautifulSoup

main_url = "http://www.alba.co.kr/"
r = requests.get(main_url)
html = BeautifulSoup(r.text, 'html.parser')
superBrand = html.find(id='MainSuperBrand')
brandList = superBrand.find('ul', {"class": "goodsBox"})
brands = brandList.find_all('li')


def save_csv(url="", name=""):
    file_name = name + '.csv'
    file = open(file_name, mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(['title', 'location', 'work_time', 'payment', 'regDate'])

    print(url)
    print(name)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    lists = soup.find('div', {"class": "goodsList"})
    table = lists.find('tbody')
    jobs = table.find_all("tr", {"class": ""})
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
    #     print(job)
    #     job_detail=job.find_all('td')
    #     print(job_detail[0].text)
    #     print(job_detail[1].find('a').find('span', {"class":"company"}).text)
    #     # print(job_detail[1].find('a').find_all('span').select('.company'))
    #     print(job_detail[2].find('span',{"class":"time"}).text)
    #     print(job_detail[3].find('span', {"class":'payIcon'}).text)
    #     print(job_detail[3].find('span', {"class": 'number'}).text)


for i, brand in enumerate(brands[:1]):
    # print(i)
    # company_name=brand.find('span', {"class":"company"})
    # company_link = brand.find('a', {"class": "goodsBox-info"})['href']

    # company_link=brand.find('a')['href']
    company_link = brand.find('a')
    company_link_url = company_link['href']
    company_name = company_link.find('span', {"class": "company"}).text
    # company_name_text=company_name.text
    # print(company_link)
    # print(company_link_url)
    # print(company_name_text)
    # print(company_link['href'])
    # print(company_name)
    # print(company_name.text)
    # print(brand.find('a'))
    # save_csv(company_link_url, company_name)
    save_csv("http://redcappizza.alba.co.kr/job/brand/", company_name)
# print(brandList)
