from flask import Flask,render_template,request
app = Flask(__name__)


@app.route("/home")
def hello():
    return render_template('index.html')
    return "why not show the design?"


if __name__ =="__main__":
        app.run(debug=True)
