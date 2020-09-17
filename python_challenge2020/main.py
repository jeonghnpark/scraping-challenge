from flask import Flask, render_template, request

app = Flask("SuperScraper")


@app.route("/")
def home():
    return render_template("contact.html")


@app.route("/hello")
def hello_fct():
    return render_template("hello.html")


@app.route("/<placeholder>")
def potato(placeholder):
    return f"hello {placeholder} "


@app.route("/kimchi")
def report():
    word = request.args.get("word")
    return render_template("report.html", word=word, sexy="sexy")


@app.route("/tomato")
def tomato():
    food_name = request.args.get("food")
    return render_template("tomato2.html", myfood=food_name)


@app.route("/test_action")
def test_action():
    username = request.args.get("un")
    # disert = request.args.get("di")
    # return render_template("favorite_desert.html", uname=username, dish=disert)
    return render_template("favorite_desert.html", uname=username)


app.run(host="localhost")
