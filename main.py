import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

spolka = input("WPISZ NAZWE SPOLKI (np. cdprojekt): ")

title = []
date = []
comment = []
counter = 30
tablica = []

for page in range(1, counter):

    site = f'https://www.stockwatch.pl/wiadomosci/walor/{spolka}/page/{page}'

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
result = pd.DataFrame(data=data).to_excel("info_giełdowe.xlsx", index=False)
