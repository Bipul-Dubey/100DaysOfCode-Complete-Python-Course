# smtp - Simple Mail Transfer Protocol
import smtplib

sender_email=""
sender_password=""
receiver_mail=""


# connection=smtplib.SMTP("smtp.gmail.com")
# connection.starttls()       # this make msg encrypted
# connection.login(user=sender_email,password=sender_password)
# connection.sendmail(from_addr=sender_email,
#                     to_addrs=receiver_email,
#                     msg="Subject:hello\n\nThis is massage content")
# connection.close()

# using with keyword so it automatically close conection
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()       # this make msg encrypted
    connection.login(user=sender_email,password=sender_password)
    connection.sendmail(from_addr=sender_email,
                        to_addrs=receiver_mail,
                        msg="Subject:hello\n\nThis is massage content")