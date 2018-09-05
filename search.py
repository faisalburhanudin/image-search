from flask import Flask, render_template

import engine

app = Flask(__name__)


@app.route("/")
def search():
    images = engine.google("faisal burhanudin")
    return render_template("search.html", images=images)
