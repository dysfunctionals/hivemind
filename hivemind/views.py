from hivemind import app
from flask import flash, redirect, render_template, request, url_for

from mcipc.query import Client as QClient

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        
        with QClient("diseased.horse", 25565) as q:
            stats = q.full_stats
        
        return render_template(
            "index.html",
            status="Unknown",
            online_players=stats["num_players"],
            total_players=stats["max_players"],
            motd=status["hostname"],
            players=["OO"],
        )
    else:
        return str(request.form)
