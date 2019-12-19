import smtplib
import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def sendEmail(subject, msg, recipientemail):
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.emailAddress, config.password)
		server.sendmail(config.emailAddress, recipientemail, text)
		server.quit()
		print("Email Sent")
	except:
		print("Email Not Sent")


subject = "NEW DEAL AVAILABLE"

msg = MIMEMultipart()
msg['From']  = config.emailAddress
msg['To'] = config.recipientemail
msg['Subject'] = subject
body = "Hello, this was sent using Python"
msg.attach(MIMEText(body,'plain'))

filename = "sample_image.jpg"
attachment = open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)
msg.attach(part)
text = msg.as_string()

sendEmail(subject, msg, config.recipientemail)
