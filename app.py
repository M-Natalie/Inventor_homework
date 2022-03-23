from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    f = open("goods.txt", "r", encoding="utf-8")
    txt = f.readlines()
    return render_template("index2.html", goods=txt)

