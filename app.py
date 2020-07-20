# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
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
        
        return render_template("results.html", json=json)

    else:
        return "Error"
