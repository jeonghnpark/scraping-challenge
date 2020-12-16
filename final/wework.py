import requests
from bs4 import BeautifulSoup


def get_job(word):
    URL = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    html = requests.get(URL)
    soup = BeautifulSoup(html.text, 'html.parser')
    ww_job = []

    jobs = soup.find_all("li", {"class": "feature"})
    for job in jobs:
        link=job.find('a')['href']
        company=job.find('span', {"class":"company"}).string
        title=job.find('span', {"class":"title"}).string
        ww_job.append({'title':title, "company":company, "link":f"https://weworkremotely.com{link}"})

    return ww_job

if __name__ == "__main__":
    jobs = get_job("python")
    [print(job['title'], job['company'], job['link']) for job in jobs]
