import smtplib
import time

# Mail Server (gmail, yahoo, hotmail), Port (default SMTP)
server = smtplib.SMTP('smtp.gmail.com', 587)
# This identifies python to the mail server
server.ehlo()
server.starttls()
server.ehlo()

# Give python credentials to login main gmail
server.login('bu7861456@gmail.com', 'nevdhoqzhzqimjxf')

target = ["bilaluddin474@gmail.com", "bilal7861456@gmail.com"]

for email in target:
    subject = "Very Informal Title"
    body = f"""
Hello {email.split("@")[0]}, YOU OWE ME MONEY

and don't forget to subscribe and like the video

-B 
    """

    msg = f"Subject: {subject} \n\n{body}"

    # Creating a draft for python to send the mail to
    server.sendmail(
        'bu7861456@gmail.com',
        email,
        msg
    )
    print(f"Email has been sent to {email}")

# We want python to exit from our account once we're done
# Python can make around 100 requests before it shuts down
server.quit()
