# flask12.py
# ref:
# http://flask.pocoo.org/

# Demo1:
# export FLASK_DEBUG=1
# export FLASK_APP=flask12.py
# flask run
# curl 127.0.0.1:5000/

# Demo2:
# python flask12.py

# Demo3:
# gunicorn wsgi

import pdb
import os
from   flask import Flask
from   flask import send_from_directory
application = Flask(__name__)
            
@application.route("/")
def home():
    return send_from_directory(os.path.join(application.root_path, 'static'),'home.html')

@application.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

from flask import render_template
@application.route("/template10/")
def template10():
    return render_template('template10.html')

@application.route("/template11/<tkr>")
def template11(tkr=None):
    return render_template('template11.html', tkr=tkr)

@application.route("/template12/")
def template12():
    mystr = 'hello'
    return render_template('template12.html', mystr=mystr)

import requests
import bs4
@application.route("/template13/")
def template13():
    myrsp     = requests.get('https://finance.yahoo.com/quote/IBM')
    soup      = bs4.BeautifulSoup(myrsp.text, "lxml")
    div_qhi_s = str(soup.find(id="quote-header-info"))
    return render_template('template13.html', mystr=div_qhi_s)

@application.route("/template14/<tkr>")
def template14(tkr='FB'):
    myrsp     = requests.get('https://finance.yahoo.com/quote/'+tkr)
    soup      = bs4.BeautifulSoup(myrsp.text, "lxml")
    div_qhi_s = str(soup.find(id="quote-header-info"))
    return render_template('template14.html', mystr=div_qhi_s)

from flask import request
@application.route("/template15/")
def template15():
    tkr       = request.args.get('tkr', 'FB')
    myrsp     = requests.get('https://finance.yahoo.com/quote/'+tkr)
    soup      = bs4.BeautifulSoup(myrsp.text, "lxml")
    div_qhi_s = str(soup.find(id="quote-header-info"))
    return render_template('template15.html', mystr=div_qhi_s)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0', port=port)
'bye'

