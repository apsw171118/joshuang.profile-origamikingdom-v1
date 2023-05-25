from flask import Flask, render_template

app = Flask(__name__)


@app.route('/discord')
def html():
    return render_template(open("Pages/discord.html").read())
