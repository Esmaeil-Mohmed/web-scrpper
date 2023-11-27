import requests
from bs4 import BeautifulSoup

def scrape_books():
    url = "https://books.toscrape.com/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the book containers
        book_containers = soup.find_all('article', class_='product_pod')

        for book in book_containers:
            # Extract book name
            book_name = book.h3.a.attrs['title']

            # Extract book rating
            book_rating = book.p.attrs['class'][1]

            # Extract book price
            book_price = book.select_one('div p.price_color').text

            print(f"Book Name: {book_name}")
            print(f"Book Rating: {book_rating}")
            print(f"Book Price: {book_price}\n")

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_books()
