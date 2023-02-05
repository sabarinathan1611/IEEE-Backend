from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'ieee.event2023@gmail.com'
app.config['MAIL_PASSWORD'] = 'wtmllyovvmsjydhy'

mail = Mail(app)

@app.route("/send_email")
def send_email():
    msg = Message(
        'Hello',
        sender='2021pecit303@gmail.com',
        recipients=['sabarinathan.project@gmail.com']
    )
    with app.open_resource("./tech.xlsx") as fp:  
        msg.attach("tech.xlsx",fp.read())  

    msg.body = "This is a test email sent from Flask"
    mail.send(msg)
    return "Email sent!"

if __name__ == '__main__':
    app.run(debug=True)

