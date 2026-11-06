import smtplib
import numpy
import keyring
import pandas as pd
from email.message import EmailMessage

class emailer:
        
    def sendEmail(self, semail, spass, remail, msgContent, sub): #sender email, sender password (use pass key for heightened data security - secure your data motherfucker), recipient email, message content, subject+
        # Build the message
        SMTP_SERVER = "smtp.gmail.com" 
        SMTP_PORT = 465     
        msg = EmailMessage()
        msg["Subject"] = sub
        msg["From"] = semail
        msg["To"] = remail
        msg.set_content(msgContent)
        print(msg)
        # Establish connection and send the email
        try:    
            #Try to connect to the server
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                # Log in to your account
                server.login(semail, spass)
                # Send the message
                server.send_message(msg)
                print("Email sent successfully!")
    
        except Exception as e:
                print(f"An error occurred: {e}")
    
    def getMessageData(self, fileName): #I only have libreoffice and this could easily be edited for excel files.
        df = pd.read_excel(fileName, engine="odf")
        return df

fup = emailer() 
mailingList = fup.getMessageData("emails.ods") #emails.ods is a libreOffice calc file that I have set up in the same folder. It contains a column of emails(RecipientEmail), the associated message(MessageContent), and the associated subject line(Subject).
MyEmail=keyring.get_credential("followups", None).username #I am using keyring for security reasons
Mypass=keyring.get_credential("followups", None).password
i=0
for x in mailingList['RecipientEmail']:
    print(x)
    fup.sendEmail(MyEmail, Mypass, x, mailingList['MessageContent'][i], mailingList['Subject'][i])
    i=i+1
