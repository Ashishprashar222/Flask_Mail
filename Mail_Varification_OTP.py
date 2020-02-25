#Email Varification Using OTP in Flask

from flask import Flask,render_template,request
from flask_mail import Mail,Message
from random import randint

app=Flask(__name__)
mail=Mail(app)

app.config["MAIL_SERVER"]='smtp.gmail.com'
app.config["MAIL_PORT"]=465
app.config["MAIL_USERNAME"]='ashishprashar37@gmail.com'
app.config['MAIL_PASSWORD']='************'                    #you have to give your password of gmail account
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)
otp=randint(000000,999999)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/verify',methods=["POST"])
def verify():
    email=request.form['email']
    msg=Message(subject='OTP',sender='ashishprashar37@gmail.com',recipients=[email])
    msg.body=str(otp)
    mail.send(msg)
    return render_template('verify.html')
@app.route('/validate',methods=['POST'])
def validate():
    user_otp=request.form['otp']
    if otp==int(user_otp):
        return "<h3>Email varification succesfull</h3>"
    return "<h3>Please Try Again</h3>"
if __name__ == '__main__':
    app.run(debug=True)