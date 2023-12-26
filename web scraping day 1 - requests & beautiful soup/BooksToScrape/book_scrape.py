import requests
from bs4 import BeautifulSoup
for i in range(1,51):
	url_to_add = f'https://books.toscrape.com/catalogue/page-{i}.html'
	url_list.append(url_to_add)
r_list = []
for url in url_list:
	r_list.append(requests.get(url))
books_info = []
for r in r_list:
    soup = BeautifulSoup(r.text, 'html.parser')
    book_articles = soup.find_all('article', class_='product_pod')
    for article in book_articles:
        title = article.h3.a['title']
        price = article.select_one('div.product_price p').text.strip()
        book_info = {'title': title, "price": price}
        books_info.append(book_info)
print(books_info)
