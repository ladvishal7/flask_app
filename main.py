from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return  render_template("home.html")
@app.route("/about")
def about():
    name = 'vishal'
    return render_template("about.html",name= name )