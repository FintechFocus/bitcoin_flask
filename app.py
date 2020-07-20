# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template, render_template_string
from flask import request
import model


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")



@app.route('/results', methods=["GET", "POST"])
def results():
    if request.method == "POST":
        id = request.form['cryptocurrency']
        
        json = model.get_coin(id)

        props = {
            "name":json['data']['coin']['name'],
            "description":model.remove_tags(json['data']['coin']['description']),
            "symbol":json['data']['coin']['symbol'],
            "history":json['data']['coin']['history'],
            "price":json['data']['coin']['price'],
            "iconUrl":json['data']['coin']['iconUrl'],
            "websiteUrl":json['data']['coin']['websiteUrl']

        }
        return render_template("results.html", props=props)

    else:
        return "Error"
