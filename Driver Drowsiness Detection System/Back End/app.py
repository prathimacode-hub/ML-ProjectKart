from flask import Flask, render_template, redirect, url_for,request
from index import func
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Start') == "Start":
            func()
            return render_template("home.html")
    else:
        return render_template("home.html")


if __name__== '__main__':
    app.run(debug=True)
