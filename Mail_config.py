from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ashishprashar37@gmail.com'
app.config['MAIL_PASSWORD'] = '********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'ashishprashar37@gmail.com', recipients = ['sonaalsarkar1997@gmail.com'])
   msg.body = "Hello sonal my first mail app"
   mail.send(msg)
   return "Mail Sent please check"

if __name__ == '__main__':
   app.run(debug = True)