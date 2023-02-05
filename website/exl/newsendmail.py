import os
import smtplib
import openpyxl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from flask import Flask

app = Flask(__name__)

@app.route("/send_email")
def send_email():
    # create an instance of MIMEMultipart
    msg = MIMEMultipart()

    # add recipient and sender email addresses
    msg['From'] = 'ieee.event2023@gmail.com'
    msg['To'] = COMMASPACE.join(['sabarinathan.project@gmail.com'])
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = 'Excel Attachment'

    # add the message body
    msg.attach(MIMEText("Here's the attached Excel file."))

    # open the Excel file
    file_path = "tech.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    # add the Excel file as an attachment
    with open(file_path, "rb") as f:
        part = MIMEBase("application", "vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition",
                        "attachment; filename= {}".format(os.path.basename(file_path)))
        msg.attach(part)

    # send the email
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ieee.event2023@gmail.com', 'pass')
    smtp.sendmail('ieee.event2023@gmail.com', ['sabarinathan.project@gmail.com'], msg.as_string())
    smtp.quit()

    return "Email sent with Excel attachment successfully!"

if __name__ == "__main__":
    app.run()
