# smtp - Simple Mail Transfer Protocol
import smtplib

my_email="smtpcheck9@gmail.com"
password="Smtp@1111"

# connection=smtplib.SMTP("smtp.gmail.com")
# connection.starttls()       # this make msg encrypted
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs="raj12kumar21@yahoo.com",
#                     msg="Subject:hello\n\nThis is massage content")
# connection.close()

# using with keyword so it automatically close conection
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()       # this make msg encrypted
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="raj12kumar21@yahoo.com",
                        msg="Subject:hello\n\nThis is massage content")