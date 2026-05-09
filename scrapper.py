import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "http://books.toscrape.com/catalogue/"

productlinks = []
data = []
c = 0

# 📚 Step 1: collect product links from multiple pages
for x in range(1, 6):

    url = f"http://books.toscrape.com/catalogue/page-{x}.html"
    k = requests.get(url).text
    soup = BeautifulSoup(k, 'html.parser')

    productlist = soup.find_all("article", {"class": "product_pod"})

    for product in productlist:
        link = product.h3.a.get('href')
        full_link = baseurl + link.replace('../../../', '')
        productlinks.append(full_link)


# 📦 Step 2: visit each product page and extract data
for link in productlinks:

    f = requests.get(link).text
    hun = BeautifulSoup(f, 'html.parser')

    # 📌 Name
    try:
        name = hun.find("h1").text.strip()
    except:
        name = None

    # 💰 Price
    try:
        price = hun.find("p", class_="price_color").text.strip()
    except:
        price = None

    # 📖 Description
    try:
        about = hun.find("div", id="product_description")
        about = about.find_next_sibling("p").text.strip()
    except:
        about = None

    # ⭐ Rating
    try:
        rating_class = hun.find("p", class_="star-rating")["class"]
        rating = rating_class[1]
    except:
        rating = None

    book = {
        "name": name,
        "price": price,
        "rating": rating,
        "about": about
    }

    data.append(book)

    c += 1
    print("completed", c)


# 📊 Step 3: convert into dataframe
df = pd.DataFrame(data)
df.to_csv("books_data.csv", index=False)