##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import smtplib
import datetime as dt
import random

now=dt.datetime.now()
current_day=now.day
current_month=now.month
data=pandas.read_csv("birthdays.csv")
data_list=[]
letter_list=["letter_1.txt","letter_2.txt","letter_3.txt"]
for index,row in data.iterrows():
    data_list.append(row.to_dict())
for i in range(len(data["name"])):
    day=data_list[i]["day"]
    month=data_list[i]["month"]
    if current_day==day and current_month==month:
        with open("quotes.txt","r") as file:
            quotes_data=file.readlines()
        quote=random.choice(quotes_data)
        name=data_list[i]["name"]
        email=data_list[i]["email"]
        letter_txt=random.choice(letter_list)
        with open(f"./letter_template/{letter_txt}") as file:
            letter=file.read()
            letter1=letter.replace("[NAME]",name)

        my_email="jeeva.nadhan.3057@gmail.com"
        password="budsrxfmdtgxwqqx"
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email,
                                msg=f"SUBJECT:HAPPY BIRTHDAY !\n\n{letter1}\n\n{quote} ")
