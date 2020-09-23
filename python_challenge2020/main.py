from flask import Flask, render_template, request, redirect

from python_challenge2020.find_job_so import get_jobs

db = {}
app = Flask("SuperScraper")


@app.route("/")
def home():
    return render_template("contact.html")


@app.route("/hello")
def hello_fct():
    return render_template("hello.html")


@app.route("/<placeholder>")
def potato(placeholder):
    return f"hello {placeholder}"


@app.route("/tomato")
def tomato():
    food_name = request.args.get("food")
    return render_template("tomato2.html", myfood=food_name)


@app.route("/report")
def report():
    word_to_find = request.args.get("word")
    if word_to_find:
        word_to_find = word_to_find.lower()
    else:
        return redirect("/")
    
    fake_db = db.get(word_to_find)
    if fake_db:
        jobs_list = fake_db
    else:
        jobs_list = get_jobs(word_to_find)
        db[word_to_find] = jobs_list
    # print(jobs_list)
    return render_template("report2.html", word_to_find=word_to_find, jobs=jobs_list)
    # print(request.args)
    # username, disert = request.args
    # username = request.args.get("un")
    # disert = request.args.get("di")
    # return render_template("favorite_desert.html", uname=username, dish=disert)
    # return render_template("favorite_desert.html", uname=username)


app.run(host="localhost")
