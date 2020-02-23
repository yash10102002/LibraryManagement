from email.message import EmailMessage
import smtplib

EMAIL = "yashkalavadiya1010@gmail.com"
PASSWORD = "9975462670"

msg = EmailMessage()

msg['Subject'] = 'Email Using python'
msg['From'] = EMAIL
msg['To'] = ["yashkalawadiya1010@gmail.com"]

message = "This message is sent using python program"
msg.set_content(message)

attachments = ['C:\\Users\\yash\\Desktop\\Web Development\\wbc.jpg']

for path in attachments:
    with open(path,'rb') as file:
        data = file.read()
        name = path.split("\\")[-1]

    msg.add_attachment(data, maintype='application', subtype='octet-stream', filename=name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

    smtp.login(EMAIL, PASSWORD)
    smtp.send_message(msg)


