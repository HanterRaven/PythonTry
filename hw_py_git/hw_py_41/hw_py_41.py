from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open("bash.csv", "a", encoding="utf-8") as f:
        writter = csv.writer(f, lineterminator="\r")
        writter.writerow((data["number"], data["date"], data["text"], data["rating"]))


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    s = soup.find_all("div", class_="quote__frame")
    for i in s:
        permalinks = i.find("a", class_="quote__header_permalink").text
        date_bash = i.find("div", class_="quote__header_date").text.strip()
        text_bash = i.find("div", class_="quote__body").text.strip()
        quote = i.find("div", class_="quote__total").text
        data = {"number": permalinks, "date": date_bash, "text": text_bash, "rating": quote}
        write_csv(data)


def main():
    url = "https://bash.im"
    get_data(get_html(url))


if __name__ == "__main__":
    main()
