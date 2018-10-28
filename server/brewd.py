'''
@brief: brewd is a flask-based xHTCPCP daemon and server, written in python3

@author: Bader Zaidan 
@version: 0.01
'''

from flask import Flask, redirect #, url_for
from pot import Pot

app = Flask(__name__)

covfefe = Pot("covfefe")

@app.route("/")
def reroute():
    #test redirect
    return redirect("pot",code=302)
    #   return "Home"

@app.route("/pot", methods = ["GET"])
def get():
    return covfefe.get()

@app.route("/pot", methods = ["HEAD"])
def head():
    return covfefe.head()

@app.route("/pot", methods = ["BREW", "POST"])
def brew():
    return covfefe.brew()

@app.route("/pot", methods = ["PROPFIND"])
def propfind():
    return covfefe.propfind() 

@app.route("/pot", methods = ["WHEN"])
def when():
    return covfefe.when()
    
@app.route("/teapot")
def teapot():
    return covfefe.teapot()

@app.route("/about")
def about():
    return covfefe.about()


if(__name__ == "__main__"):
    app.run(host=covfefe.host, port=covfefe.port,  debug=True)
