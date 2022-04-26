#!/usr/bin/python3

import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep


email = "YOUR@EMAIL.COM"
pas = "YOUR_EMAIL_PASSWORD"

sms_gateway = 'PHONE_NUMBER@tmomail.net'

#Every email provider has a different smtp. Most have the same port.
#Uncomment the SMTP provider that you would like to use if you are sending from Gmail or Microsoft Outlook or add another one.

#smtp = "smtp.gmail.com" 
#smtp =  "smtp.office365.com"
port = 587

# This will start our email server
server = smtplib.SMTP(smtp,port

# Starting the server most smtp servers use TLS encryption
server.starttls()

# Now we need to login
server.login(email,pas)

# Now we use the MIME module to structure our message.
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = sms_gateway
                      
# Make sure you add a new line in the subject
msg['Subject'] = "Hey Friend"
                      
# Make sure you also add new lines to your body
body = """
Hey there, bro
hope you are prepared to have your phone blown up.

eat my shorts.
(ﾉಠдಠ)ﾉ︵┻━┻
    
    🎤
        """
                      
# Then, attach that body. You can also send html content if you 
# change 'plain' to 'html' however cell phones cannot receive HTML content as an SMS or MMS
msg.attach(MIMEText(body, 'plain'))

sms = msg.as_string()

repeat = 1

while repeat <= 2000:

    server.sendmail(email,sms_gateway,sms)
    print(repeat)
    sleep(6)
    repeat = repeat + 1

# lastly quit the server
server.quit()
