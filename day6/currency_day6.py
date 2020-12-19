import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

url = "https://www.iban.com/currency-codes"

def ask_first_country():
  try:
    return int(input("# :"))
  except ValueError:
    print("That was not a number")
    print("Choose a country by number.\n")
    return ask_first_country()


def main():
    global request
    try:
        request = requests.get(url)
        if request.status_code == 200:
            pass
        else:
            print(url, "is down!")
    except:
        print(url, "is down!")

    html = request.text
    soup = BeautifulSoup(html, 'html.parser')
    trs = soup.find_all('tr')
    trs = trs[1:]

    cur_list = []
    for i, tr in enumerate(trs):
        cur_info = {}
        tds = tr.find_all('td')
        cur_info['Country'] = tds[0].text.lower().capitalize()
        cur_info['Code'] = tds[2].text
        cur_list.append(cur_info)
    print("Currency Convertor")
    for i, country in enumerate(cur_list):
        print(f"# {i} {country['Country']}")

    print("Where are you from? Choose a country by number.\n")
    num=ask_first_country()
    print(f"{cur_list[num]['Country']}")
    print("\nNow Choose another country")
    num2=ask_first_country()
    print(f"{cur_list[num2]['Country']}")

    while 1:
        try:
            print(f"How many {cur_list[num]['Code']} do you want to convert to {cur_list[num2]['Code']}?\n")
            amount = float(input(":"))
            url2=f"https://transferwise.com/gb/currency-converter/{cur_list[num]['Code']}-to-{cur_list[num2]['Code']}-rate?amount={amount}"
            convertor_html = requests.get(url2)
            convertor_soup = BeautifulSoup(convertor_html.text, "html.parser")
            rate=convertor_soup.find("span", {"class":"text-success"})
            if rate:
              rate=rate.string
              print(f"{cur_list[num]['Code']} {round(amount,2)} is {format_currency(float(rate)*amount, 'KRW', locale='ko_KR')}")
            else:
              print("Not able to refer to currency information")
            break
        except ValueError:
            print("That was not a number")
            continue


main()