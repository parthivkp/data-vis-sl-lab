from flask import Flask,render_template,session,request
import time

app=Flask(__name__)

app.secret_key="secret"

@app.route("/",methods=['GET','POST'])

def index():
	try:
		balance=session["balance"]
		count=session["count"]
	except KeyError:
	    balance=session["balance"]=7000
	    count=session["count"]=0

	if request.method=='GET':
		return render_template("web.html",balance=balance,msg="WELCOME!!!")

	if (request.method=='POST'):
		if request.form["action"]=="withdraw":
		  balance=balance-int(request.form["amount"])
		  session["balance"]=balance
		  return render_template("web.html",balance=balance ,msg="withdraw succefull!!")
		else:
			
		  balance=balance+int(request.form["amount"])
		  session["balance"]=balance
		  return render_template("web.html",balance=balance, msg="deposit succefull!!")  

			

    
        


if __name__=='__main__':
    app.run(host='0.0.0.0', port=12000, debug=True)


































