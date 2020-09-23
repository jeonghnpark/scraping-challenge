from flask import Flask, render_template, request, redirect

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
    return render_template("report2.html", word_to_find=word_to_find)
    # print(request.args)
    # username, disert = request.args
    # username = request.args.get("un")
    # disert = request.args.get("di")
    # return render_template("favorite_desert.html", uname=username, dish=disert)
    # return render_template("favorite_desert.html", uname=username)


app.run(host="localhost")
