import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"


def main():
    # url = "https://www.iban.com/currency-codes"
    # url = "https://www.iban.com/currodes"
    global request
    try:
        request = requests.get(url)
        if request.status_code == 200:
            # print(url, "is up!")
            # print("Hello, Select a country number: ")
            pass
        else:
            print(url, "is down!")
            # sys.exit()
    except:
        print(url, "is down!")
        # sys.exit()

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
    print("Hello, please choose a country by number")
    for i, country in enumerate(cur_list):
        print(f"# {i} {country['Country']}")

    while 1:
        try:
            num = int(input("# :"))
        except ValueError as ve:
            print("That was not a number")
            continue

        if num > len(cur_list) - 1:
            print("Choose a number from the list ")
            continue
        else:
            print(f"You chose {cur_list[num]['Country']} ")
            print(f"The country code is {cur_list[num]['Code']}")
            break


main()
