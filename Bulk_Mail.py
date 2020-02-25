from flask import Flask
from flask_mail import Mail,Message
app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='ashishprashar37@gmail.com'
app.config['MAIL_PASSWORD']='********'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

users=[{'name':'sonal','email':'sonaalsarkar1996@gmail.com'},{'name':'suresh','email':'sureshdhaka567@gmail.com'},{'name':'ankita','email':'ankitagorai123@gmail.com'}]
mail=Mail(app)
@app.route('/')
def index():
    with mail.connect()as con:
        for user in users:
            message="hey %s" %user['name'] +" ,i sent you the bulk mail for testing..my first bulk mail by using Flask"
            msgs=Message(recipients=[user['email']],body=message,subject='hello',sender='ashishprashar37@gmail.com')
            con.send(msgs)
        return "mail Sent"
if __name__ == '__main__':
    app.run(debug=True)