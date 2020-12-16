import csv


def save_to_file(jobs):
    file = open('jobs.csv', 'w')
    writer = csv.writer(file)
    writer.writerow(['title', 'company', 'link'])

    for job in jobs:
        writer.writerow([job['title'], job['company'], job['link']])
    return


if __name__ == "__main__":
    jobs = [{'title': 'this title', 'company': 'naver', 'link': 'naver.com'}]
    save_to_file(jobs)
