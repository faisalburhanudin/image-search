from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def search():
    return render_template("search.html", images=range(12))
