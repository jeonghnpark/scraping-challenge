import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/jobs?q=python"
# url = "http://www.naver.com"
html = requests.get(url, )

soup = BeautifulSoup(html.text, 'html.parser')
# print(soup)

list_result = soup.find('div', {"class": "listResults"})

jobs = list_result.find_all('div', {"class": "-job"})

jobs_list = []
for job in jobs[:1]:
    link = job.find('h2').find('a')

    job_postion = link['title']
    name_location = job.find('h3').find_all('span')
    # print(location)
    print(len(name_location))
    print(name_location[0])
    # print(name_location[1])
    job_found = {}
    # job_found['job_postion'] = job_postion
    # job_found['location'] = location
    # jobs_list.append(job_found)

# print(jobs_list)
