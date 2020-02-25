from flask import Flask
from flask_mail import Mail,Message

app = Flask(__name__)

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'ashishprashar37@gmail.com'          #give your Email id
app.config['MAIL_PASSWORD'] = '*************'              #give your email password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
@app.route("/")
def index():
    msg = Message(subject="hello", body="hello", sender="ashishprashar37@gmail.com", recipients=["sureshdhaka567@gmail.com"])
    with app.open_resource("/Users/Ashish/Desktop/images.png") as fp:
        msg.attach("images.png", "image/png", fp.read())
        mail.send(msg)
    return "sent"

if __name__ == "__main__":
    app.run(debug=True)