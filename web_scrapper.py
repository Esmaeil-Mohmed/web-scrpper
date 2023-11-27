import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")

soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article")

for book in books:
    title = book.h3.a["title"]
    rating = book.p["class"][1]
    price = book.select_one("p.price_color").text
    print(f"Book title: '{title}', Rating: '{rating}' stars, Price: {price}")