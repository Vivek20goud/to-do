from flask import Flask,render_template

app = Flask(__name__)

@app.route("/home")
def Homepage():
    return render_template('home.html')

@app.route("/login")
def loginpage():
    return render_template('login.html')  


@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/complete")
def complete():
    return render_template('complete.html')


@app.route("/present")
def present():
    return render_template('present.html')

if __name__=='__main__':
    app.run(debug=True,port=6139)