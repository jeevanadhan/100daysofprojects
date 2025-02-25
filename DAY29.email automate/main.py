import smtplib
my_email="jeeva.nadhan.3057@gmail.com"
password="budsrxfmdtgxwqqx"
with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="senderpython063@gmail.com",
                        msg="SUBJECT:nothing\n\n hello this is from ____")