from flask import Flask

app = Flask("APP")


@app.route("/")
def home():
    return "Return"


@app.route("/<username>")
def potato():
    return "placehoder{}"


app.run(host="localhost")
