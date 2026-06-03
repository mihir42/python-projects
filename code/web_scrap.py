import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

with open("quotes.txt", "w", encoding="utf-8") as f:
    for quote, author in zip(quotes, authors):
        print(quote.text, "-", author.text)
        f.write(quote.text + "-" + author.text + "\n")


        


    

