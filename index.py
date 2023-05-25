from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def html():
    return render_template(open("Pages/index.html").read())