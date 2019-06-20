import smtplib
import config

def sendEmail(subject,msg,recipientemail):
	try:
		server=smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.emailAddress,config.password)
		message= 'Subject: {} \n\n {}'.format(subject,msg)
		server.sendmail(config.emailAddress,recipientemail,message)
		server.quit()
		print("Email Sent")
	except:
		print("Email Not Sent")
		
subject="NEW DEAL AVAILABLE"
msg="2 For 1 for all mains on our menu"
recipientemailaddress="RECIPIENT EMAIL"
sendEmail(subject,msg,recipientemailaddress)