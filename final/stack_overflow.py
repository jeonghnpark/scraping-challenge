import requests
from bs4 import BeautifulSoup


def get_job(word):
    URL = f"https://stackoverflow.com/jobs?r=true&q={word}"
    html = requests.get(URL)
    soup = BeautifulSoup(html.text, 'html.parser')
    # soup = BeautifulSoup(open('so.html', encoding='utf-8'), 'html.parser')
    pagination = soup.find('div', {"class": "s-pagination"})
    pages = pagination.find_all("a")
    # print(len(pages))
    last_page = len(pages) - 1

    # listResults=soup.find("div", {"class":"listResults"})
    # jobs=listResults.find_all("h2", {"class":"mb4"})
    # # [print(job) for job in jobs]

    # print(len(jobs))
    # for job in jobs[0]:
    #     # title_link=job.find("h2").find("a")
    #     # title=title_link['title']
    #     # link=title_link['link']
    #     # print(title, link)
    #     h2=job.find('h2')
    #     print(h2)
    #     # print(job.find('h2').find('a')['href'])
    so_job = []
    for p in range(last_page):
    # for p in range(1):
        page_num = p + 1
        url = f"https://stackoverflow.com/jobs?q={word}&r=true&pg={page_num}"
        # url="https://stackoverflow.com/jobs?r=true&q=python"
        # URL = "https://stackoverflow.com/jobs?r=true&q=python"
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        # soup = BeautifulSoup(open('so.html', encoding='utf-8'), 'html.parser')
        listResults = soup.find("div", {"class": "listResults"})
        # print(len(listResults))
        jobs = listResults.find_all("div", {"class": "-job"})
        for job in jobs:
            # print(job)
            # print(job.find('a').string)
            link = job.find('a', {"class": "s-link"})['href']
            title = job.find('a', {"class": "s-link"})['title']
            company = job.find('h3').find('span').string
            # print(link)
            # print(title)
            # print(company)
            so_job.append({'title': title, 'company': company, 'link': f"https://stackoverflow.com{link}"})

    return so_job
