from hivemind import app
from flask import flash, redirect, render_template, request, url_for


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        return "OOF"
