# 📚 Task 1 – Web Scraping with BeautifulSoup

Scrapes book data from [books.toscrape.com](https://books.toscrape.com/) and exports it as a CSV file.

## 🔍 What It Does
- Sends an HTTP GET request to the website
- Parses the HTML with BeautifulSoup
- Extracts **Title, Price, Rating, Availability, and Product URL** for each book
- Saves all records to `books_dataset.csv`

## 📁 Folder Structure
```
task1_web_scraping/
├── scraper.py           ← Main script
├── books_dataset.csv    ← Output (auto-generated on run)
├── requirements.txt     ← Dependencies
└── README.md
```

## 🚀 How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the scraper
python scraper.py
```

## 📦 Libraries Used
| Library | Purpose |
|---------|---------|
| `requests` | Fetch the web page |
| `beautifulsoup4` | Parse HTML content |
| `pandas` | Structure and export data |

## 📊 Output Sample
| Title | Price | Rating | Availability |
|-------|-------|--------|--------------|
| A Light in the Attic | £51.77 | Three | In stock |
| Tipping the Velvet | £53.74 | One | In stock |

> **Note:** The site has 20 books per page. This script scrapes page 1 only.

---
*CodeAlpha Data Analytics Internship – Task 1*
