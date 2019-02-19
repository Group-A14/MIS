from flask import Flask
from flask_mail import Mail, Message
import random

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dasarigowthami25@gmail.com'
app.config['MAIL_PASSWORD'] = '$eeN@#G78'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
	chars="0123456789qwertyuioplmnbvcxzasdfghjk"
	password=random.random();
	msg = Message('Hello', sender = 'dasarigowthami25@gmail.com', recipients = ['gowthami202s@gmail.com'])
	msg.body = "Your OTP is "+password
	mail.send(msg)
	return "Check your Mail for OTP"

if __name__ == '__main__':
	app.run(debug = True)