"""
Task 1 – Web Scraping
---------------------
Scrapes book data (title, price, rating, availability, URL)
from https://books.toscrape.com/ and saves it to books_dataset.csv
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = "https://books.toscrape.com/"
OUTPUT_FILE = "books_dataset.csv"


def scrape_books(url: str) -> list[dict]:
    """Fetch and parse all books from the homepage."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    print(f"Page title : {soup.title.text.strip()}")
    print(f"Status code: {response.status_code}")

    book_cards = soup.find_all("article", class_="product_pod")
    print(f"Books found: {len(book_cards)}")

    book_data = []
    for book in book_cards:
        title        = book.h3.a["title"]
        price        = book.find("p", class_="price_color").text.strip()
        rating       = book.find("p")["class"][1]          # e.g. "Three"
        availability = book.find("p", class_="instock availability").text.strip()
        link         = "https://books.toscrape.com/" + book.h3.a["href"]

        book_data.append({
            "Title":        title,
            "Price":        price,
            "Rating":       rating,
            "Availability": availability,
            "Product URL":  link,
        })

    return book_data


def main():
    data = scrape_books(URL)

    df = pd.DataFrame(data)
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"\nDataset shape : {df.shape}")
    print(df.head())
    print(f"\nTotal books saved: {len(data)}")
    print(f"Output saved to  : {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
