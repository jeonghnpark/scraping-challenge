import requests
from bs4 import BeautifulSoup


def get_job(word):
    URL = f"https://remoteok.io/remote-dev+{word}-jobs"
    URL = "https://remoteok.io/remote-dev+python-jobs"
    print(URL)
    # URL = f"https://weworkremotely.com/remote-jobs/search?term={word}"

    html = requests.get(URL)
    soup = BeautifulSoup(html.text, 'html.parser')
    rw_job = []
    # jobs_board=soup.find('table', {"id":"jobsboard"})
    jobs_board = soup.find('div', {"class": "container"})

    jobs = jobs_board.find_all("tr", {"class": "job"})
    for job in jobs[:5]:
        link=job['data-url']
        company=job['data-company']
        title=job['data-search']
        rw_job.append({'title':title, "company":company, "link":f"https://weworkremotely.com{link}"})

    return rw_job


if __name__ == "__main__":
    jobs = get_job("python")
    print(jobs)
    # [print(job['title'], job['company'], job['link']) for job in jobs]
