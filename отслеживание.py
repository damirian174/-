import requests
from bs4 import BeautifulSoup
import time

BitCoin_Rub = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0&aqs=chrome..69i57j35i39j0i131i395i433j0i395j0i131i395i433l2j0i395l4.10847j1j7&sourceid=chrome&ie=UTF-8'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

def check_currency():
    full_page = requests.get(BitCoin_Rub,headers=headers)

    soup = BeautifulSoup(full_page.content, 'html.parser')

    convert = soup.findAll("span", {"class":"DFlfde", "class":"SwHCTb", "data-precision":2})

    print("Сейчас курс 1 биткоина = "+convert[0].text)
    time.sleep(3)
    check_currency()

check_currency()
