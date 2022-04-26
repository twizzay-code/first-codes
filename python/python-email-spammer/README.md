# SMTP-Spammer
I used this repo to spam my brother with text messages.

The heart of this repo is just a simple Python script that creates a message and encodes it into MIME format using smtplib.
After it has been encoded it sends this message as a text message through email.

The end of the Python script has a "while loop" that repeats sending the message 2000 times.

> NOTE: Most email providers will mark your email address as spam if you send the exact same email 
> in quick repeated succession. It's best to use a throwaway email address for this or if you have
> the means, host your own SMTP server. Im not responsible for what you do or what happens after you do it.

### In order for this to work for you, you will need to edit the file "ryanrevenge.py" and include your own message, email addresses and passwords.
