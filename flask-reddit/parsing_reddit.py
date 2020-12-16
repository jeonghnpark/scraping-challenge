from bs4 import BeautifulSoup
import requests


def transform_int(e):
    if e[-1] == 'k':
        return float(e[:-1].replace(",", "")) * 1000
    else:
        return float(e.replace(",", ""))


subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]

url = "https://www.reddit.com/r/rust/top/?t=month"
file = "rust.html"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

html = requests.get(url, headers=headers)

# soup=BeautifulSoup(open(file, 'r', encoding='utf-8'), "html.parser")
# html=requests.get('file://rust.html', headers=headers)
soup = BeautifulSoup(html.text, "html.parser")
threads = soup.find('div', {"class": "rpBJOHq2PR60pnwJlUyP0"}).find_all('div')
threads = soup.find_all('div', {"class": "_1oQyIsiPHYt6nx7VOmd1sz"})
# print(len(threads))

total_items = []
for subreddit in subreddits[2:5]:
    sub_items = []
    url = f"https://www.reddit.com/r/{subreddit}/top/?t=month"
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    threads = soup.find_all('div', {"class": "_1oQyIsiPHYt6nx7VOmd1sz"})

    cnt = 0
    for thread in threads:
        vote = thread.find('div', {"class": "_1rZYMD_4xY3gRcSS3p8ODO"})
        title = thread.find('h3', {"class": "_eYtD2XCVieq6emjKBH3m"})
        link = thread.find('a')

        if vote is not None and title is not None and link is not None:
            vote_float = transform_int(vote.text)

            sub_items.append({'vote': vote_float, 'title': title.text, 'link': link['href'], 'subreddit': subreddit})

        ## temporary code
        # if len(sub_items) >10:
        #     break

    # for item in sub_items:
    #     print(item['vote'])
    #     print(item['title'])
    #     print(item['link'])

    sorted_items = sorted(sub_items, key=lambda thread: (thread['vote']), reverse=True)

    sorted_items = sorted_items[:3]  # largest 4
    total_items += sorted_items

for item in total_items:
    print(item['vote'])
    print(item['title'])
    print(item['link'])
    print(item['subreddit'])

sorted_total_items = sorted(total_items, key=lambda thread: (thread['vote']), reverse=True)
print("\n\nAfter sorted")
for item in sorted_total_items:
    print(item['vote'])
    print(item['title'])
    print(item['link'])
    print(item['subreddit'])
