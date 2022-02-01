import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import pandas as pd
import openpyxl as px

gmail_address = 'marcin.automatyzacje@gmail.com'
password = 'yt5'

title = []
date = []
comment = []

def send_email_alert_new():
    subject = f'TOREBKA JEST TAŃSZA!!!!!!!!!!!!!!!!'

    msg = MIMEMultipart()
    msg['From'] = gmail_address
    msg['To'] = gmail_address
    msg['Subject'] = subject

    body = f'https://www.eobuwie.com.pl/torebka-guess-cessily-ev-hwev76-79110-bla.html?utm_source=rtbhouse&utm_medium=retargeting&utm_campaign=rtbhouse-retargeting'
    msg.attach(MIMEText(body, 'plain'))

    part = MIMEBase('application', 'octet-stream')

    text = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_address, password)
    server.sendmail(gmail_address, gmail_address, text)
    server.quit()


counter = 30
tablica = []

for page in range(1, counter):

    site = f'https://www.stockwatch.pl/wiadomosci/walor/cdprojekt/page/{page}'

    try:
        page = requests.get(site)

        if page.status_code == 200:

            soup = BeautifulSoup(page.content, "html.parser")


            for seq_title in soup.findAll(class_='post postList'):

                title.append(seq_title.find('a', class_='title').text)
                comment.append(seq_title.find(class_='leadr').text.strip())
                date.append(seq_title.find("time").text[0:10])





            godzina = time.localtime()
            aktualna = time.strftime("%H:%M:%S", time.localtime())

        else:
            print(f'strona nie odpowiada')
            continue

    except Exception as e:
        print(f'błąd: {e}')
        time.sleep(5)

data = ({"date": date,"title": title,"comment": comment})
result = pd.DataFrame(data=data).to_csv("info_giełdowe.csv", sep=";")

print(data)