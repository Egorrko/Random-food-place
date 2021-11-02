from flask import redirect, render_template, request, url_for

from app.common import config

from . import routes


@routes.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return redirect(url_for('routes.city', city=request.form["city"]))
    else:
        return render_template('index.html', config=config)
