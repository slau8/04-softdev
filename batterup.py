'''
Shannon Lau
SoftDev1 Period 7
HW #04: Fill Up Yer Flask
2017-09-20
'''

from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home_base():
    ret = "<div style='text-align:center;'>"
    ret += "Batter up!"
    ret += "<p>"
    ret += "<a href='/first_base'><button>BUNT</button></a>"
    ret += "<a href='/second_base'><button>CONTACT</button></a>"
    ret += "<a href='/third_base'><button>POWER</button></a>"
    ret += "</p>"
    ret += "</div>"
    return ret

@app.route('/first_base')
def first_base():
    ret = "<div style='text-align:center;'>"
    ret += safe_or_out() + " at first!"
    ret += "</div>"
    return ret

@app.route('/second_base')
def second_base():
    ret = "<div style='text-align:center;'>"
    ret += safe_or_out() + " at second!"
    ret += "</div>"
    return ret

@app.route('/third_base')
def third_base():
    ret = "<div style='text-align:center;'>"
    ret += safe_or_out() + " at third!"
    ret += "</div>"
    return ret

#return random status of batter
def safe_or_out():
    if random.randint(0,1) == 0:
        status = "Safe"
    else:
        status = "Out"
    return status

if __name__ == "__main__":
    app.debug = True
    app.run()
