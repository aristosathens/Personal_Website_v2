# Aristos Athens

'''
    Send emails programatically.
    Use dummy account: Aristos.Website, VerySecurePassword
'''

import smtplib 
from email.mime.multipart import MIMEMultipart

def send_email(sender, subject, message):
    '''
        Send email from aristos.website to aristos.a.athens
    '''
    s = smtplib.SMTP('smtp.gmail.com', 587) # creates SMTP session 
    s.starttls() # start TLS for security 
    s.login("Aristos.Website@gmail.com", "VerySecurePassword") 
    
    # sending the mail 
    message = MIMEMultipart(message)
    message['From'] = sender
    message['Subject'] = subject
    s.sendmail("aristos.website@gmail.com", "aristos.a.athens@gmail.com", message.as_string()) 
    
    # terminate the session 
    s.quit() 