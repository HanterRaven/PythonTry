from bs4 import BeautifulSoup
import requests


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    t = soup.find_all("div", class_="model-price-range")
    price = []
    s_price = []
    for i in t:
        test2 = i.find("a").text
        test2 = "".join(test2.split())
        test2 = test2.rstrip("р.")
        price.append(test2.split("до"))
        if len(price[0]) == 2:
            s_price.append((int(str(price[0][0])) + int(str(price[0][1]))) / 2)
        else:
            s_price.append(float(price[0][0]))
        price.pop(0)
    return s_price


def main():
    price_itog = []
    last = True
    index_page = 0
    sum = 0
    while last:
        url = f"https://www.e-katalog.ru/list/206/{index_page}/"
        price_itog.append(get_data(get_html(url)))
        if len(price_itog[index_page]) == 0:
            last = False
            price_itog.pop(index_page)
        else:
            index_page += 1
    index_price = 0
    for i in range(len((price_itog))):
        # print(i, end=" == ")
        for j in range(len(price_itog[i])):
            sum += price_itog[i][j]
            index_price += 1
        #     print(price_itog[i][j], end=" --- ")
        # print()
    midle_price = sum / index_price
    print(f"Средняя цена всех фотоаппаратов = {round(midle_price, 2)}р.")


if __name__ == "__main__":
    main()
