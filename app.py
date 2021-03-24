from flask import *
from mail import *
# from db import *

app = Flask(__name__)

@app.route('/')
def welcome(): 
    return redirect(url_for('home'))  

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == "POST":
        user_mail = request.form['email']
        content = "helloworld"
        send_email(user_mail,content)
    return redirect('/')

if __name__ == "__main__": 
    app.run(host= "0.0.0.0", port=3000, debug = True)
