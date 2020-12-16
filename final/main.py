"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

import requests
from flask import Flask, render_template, request, redirect, send_file
from bs4 import BeautifulSoup
from stack_overflow import get_job as so_job
from wework import get_job as ww_job
from save import save_to_file

db = {}

app = Flask("remote_job")


@app.route("/remote_job")
def remote_job():
    word = request.args.get('word')
    word = word.lower()
    job_num = 0
    # jobs=[{'title': "full-stack develop", 'company': "air bnb", 'link': "daum.net"}]
    if word in db:
        jobs = db.get(word)
    else:
        jobs=so_job(word)+ww_job(word)
        db[word] = jobs
        jobs = db.get(word)

    return render_template("remote_job.html", word=word, job_num=len(jobs), jobs=jobs)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file('jobs.csv', as_attachment=True)

    except:
        return redirect("/")


app.run(host="localhost")
