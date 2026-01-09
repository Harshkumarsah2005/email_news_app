import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 587

    sender_email = "hk031848@gmail.com"
    password = "odlm pemp drbu etrj"
    receiver_email = "hk031848@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        
    print("Email sent successfully!")