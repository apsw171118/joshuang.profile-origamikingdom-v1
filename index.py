from flask import Flask, render_template

origamikingdom = Flask(__name__, templates='/Pages')

@origamikingdom.route('/discord')
def html():
    return render_template(open("discord.html").read())

@origamikingom.route('/htmltest')
def html():
    return 'html'
