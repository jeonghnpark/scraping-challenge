import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

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

fake_db = {}


def transform_int(e):
    if e[-1] == 'k':
        return int(float(e[:-1].replace(",", "")) * 1000)
    else:
        return int(float(e.replace(",", "").replace('•', "0")))


def get_threads(reddit_list):
    """
    :param reddit_list:str
    :return: list of thread of dict type sorted by vote number
    """

    total_items = []

    for subreddit in reddit_list:

        if subreddit not in fake_db:
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
                    vote_int = transform_int(vote.text)
                    sub_items.append(
                        {'vote': vote_int, 'title': title.text, 'link': link['href'], 'subreddit': subreddit})

            sorted_items = sorted(sub_items, key=lambda thread: (thread['vote']), reverse=True)
            sorted_items = sorted_items[:4]  # largest 4
            fake_db[subreddit] = sorted_items
            total_items += fake_db[subreddit]
        else:
            total_items += fake_db[subreddit]

    sorted_total_items = sorted(total_items, key=lambda thread: (thread['vote']), reverse=True)
    return sorted_total_items


app = Flask("DayEleven")


@app.route("/")
def home():
    return render_template("home.html", subreddits=subreddits)


@app.route("/read")
def read():
    # print(request.args)
    subreddits = request.args
    # print("java on off=", subreddits.get('javascript'))
    # print("list -> ", subreddits.items())
    reddit_list = []
    # for key, value in subreddits.items():
    #     print(key, value)
    #     url = f"https://www.reddit.com/r/{key}/top/?t=month"
    #     html = requests.get(url, headers=headers)
    #     print(html.text)
    # reddit_list.append(result)
    # print(dir(subreddits))
    # for subreddit in subreddits:
    # print(dir(subreddit))

    for key, value in subreddits.items():
        reddit_list.append(key)

    threads = get_threads(reddit_list)

    # return render_template("read.html", subreddits=subreddits.items(), threads=threads)
    return render_template("read.html", subreddits=reddit_list, threads=get_threads(reddit_list))


# @app.route("/read")
# def read():
#     req_args = request.args
#     reddit_list = []
#     for key, value in req_args.items():
#         reddit_list.append(key)
#     # threads = get_threads(reddit_list)
#     threads=[{'vote':'123', 'link':"nvaer.com", 'title': 'title is title', 'subreddits': 'javascript'}]
#     return render_template("read.html", subreddits=reddit_list, threads=threads)

app.run(host="localhost")
