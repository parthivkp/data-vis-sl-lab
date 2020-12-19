from flask import Flask,render_template,session,request
import time

app=Flask(__name__)

app.secret_key="secret"

@app.route("/",methods=['GET','POST'])

def index():
    if request.method == "GET":
		return render_template("web.html",balance=3000)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=12000, debug=True)

































