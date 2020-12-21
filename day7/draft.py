import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"


def save_csv(url="", name=""):
    name = name.replace('/', '')  # Filename should not contain '/'
    file_name = name + '.csv'
    file = open(file_name, mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(['title', 'location', 'work_time', 'payment', 'regDate'])

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    lists = soup.find('div', {"class": "goodsList"})
    table = lists.find('tbody')
    jobs = table.find_all("tr", {"class": ["divide", ""]})

    for job in jobs[:]:
        job_detail = job.find_all('td')
        if job_detail is not None:
            job = {'title': job_detail[1].find('a').find('span', {"class": "company"}).text,
                   'location': job_detail[0].text, 'work_time': job_detail[2].find('span', {"class": "time"}).text,
                   'payment': job_detail[3].find('span', {"class": 'payIcon'}).text + job_detail[3].find('span', {
                       "class": 'number'}).text, 'regDate': job_detail[4].text}
            writer.writerow([job['title'], job['location'], job['work_time'], job['payment'], job['regDate']])
        else:
            writer.writerow('No available jobs')

    file.close()


r = requests.get(alba_url)
html = BeautifulSoup(r.text, 'html.parser')
superBrand = html.find(id='MainSuperBrand')
brandList = superBrand.find('ul', {"class": "goodsBox"})
brands = brandList.find_all('li')

for i, brand in enumerate(brands[:]):
    company_link = brand.find('a')
    company_link_url = company_link['href']
    try:  # In case last item, we skip
        company_name = company_link.find('span', {"class": "company"}).text
        save_csv(company_link_url, company_name)
    except:
        pass
    print(company_name)
