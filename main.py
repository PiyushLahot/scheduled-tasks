import pandas as pd
import smtplib
import random as rnd
import datetime as dt
import os

email_id = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
df=pd.read_csv('birthdays.csv')

dict_df=df.to_dict(orient='records')
letter_temp=[]

print(dict_df)
now=dt.datetime.now()
with open("./letter_templates/letter_1.txt") as f:
    letter = f.read()
    letter_temp.append(letter)
with open("./letter_templates/letter_2.txt") as f:
    letter = f.read()
    letter_temp.append(letter)
with open("./letter_templates/letter_3.txt") as f:
    letter = f.read()
    letter_temp.append(letter)

for k in dict_df:
    if k["month"]==now.month and k["day"]==now.day:
        ran_letter=rnd.choice(letter_temp)
        ran_letter=ran_letter.replace("[NAME]",k["name"])
        ran_letter=ran_letter.replace("Angela","Piyush")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email_id,password=password)
            connection.sendmail(from_addr=email_id,to_addrs=k["email"],
                                msg=f"Subject: Happy Birthday {k["name"]}\n\n{ran_letter}")




