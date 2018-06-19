import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'absurdjones@gmail.com'
email_password = 'look to #00FF00'
email_send = 'dodge84@live.co.uk'

subject = 'Test Email'

#set the from/to/subject of the email
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

#attach the body of the msg
body = 'Hi there, Morgan is sending this email from Python code to practice using SMTP!'
msg.attach(MIMEText(body,'plain'))

#read the file in as a binary
filename='test_attachment.txt'
attachment  = open(filename,'rb')

#encode in base64 and add the file to the msg
part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)
msg.attach(part)

#to string the msg
text = msg.as_string()

#login to gmail server on port 587 using my email & password
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)

#send the email
server.sendmail(email_user,email_send,text)
server.quit()

#close the file
attachment.close()
