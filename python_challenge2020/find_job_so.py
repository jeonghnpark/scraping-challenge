import requests
from bs4 import BeautifulSoup


def get_last_page(word):
    url = f"https://stackoverflow.com/jobs?q={word}"
    # url = "http://www.naver.com"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    # TODO: how about soup is None
    pages = soup.find('div', {"class": "s-pagination"})
    # TODO: how about pages is None
    last_pages = pages.find_all('a')
    # print(last_pages)
    # print(type(last_pages))
    last_page = 0
    # check is next

    if last_pages[-1].find('span').get_text(strip=True) == 'next':
        last_page = last_pages[-2].find('span').get_text(strip=True)
    else:
        last_page = last_pages[-1].find('span').get_text(strip=True)

    return int(last_page)


def get_jobs(word):
    last_page = get_last_page(word)
    last_page = min(int(last_page), 2)
    jobs_list = []

    for p_num, page in enumerate(range(last_page)):
        url_page = f"https://stackoverflow.com/jobs?q={word}&pg={page + 1}"
        html = requests.get(url_page)
        soup = BeautifulSoup(html.text, 'html.parser')
        # print(soup)
        list_result = soup.find('div', {"class": "listResults"})
        jobs = list_result.find_all('div', {"class": "-job"})
        print(f"page {p_num + 1} is scrapping...{len(jobs)} job(s) found")
        for i, job in enumerate(jobs):
            link = job.find('h2').find('a')
            job_position = link['title']
            link_url = link['href']
            # print(i, job_position)
            name, location = job.find('h3').find_all('span', recursive=False)

            job_found = {'job_position': job_position, 'name': name.get_text(strip=True),
                         'location': location.get_text(strip=True),
                         'link_url': f'https://stackoverflow.com/{link_url}'}
            jobs_list.append(job_found)

    return jobs_list


if __name__ == '__main__':
    print(get_jobs('python'))
