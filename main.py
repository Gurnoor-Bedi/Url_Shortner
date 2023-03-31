import pyshorteners
from flask import Flask,request,redirect,render_template
app=Flask(__name__)
s=pyshorteners.Shortener()
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/shorten",methods=["POST"])
def shorten():
    url=request.form["Url"]
    short_url=s.tinyurl.short("url")
    return render_template("result.html",short_url=short_url)
if __name__=="__main__":
    app.run()
