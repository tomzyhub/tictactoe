from flask import Flask,render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World, Tomzy is Here to Stay!"


@app.route("/check")
def check():
#return </title> calculator</title>
    a = input( "enter name:" )
    print(a, "your name is")

    print(len(a))
    print('letters long')




if __name__ =="__main__":
        app.run(debug=True)
