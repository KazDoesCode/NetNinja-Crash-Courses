import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"


x = requests.get(url)

html_content = x.content

def get_titles(parser: BeautifulSoup, css_selector:str)->list:
    titles = []
    search_query = parser.select(css_selector)
    for title in search_query:
        titles.append(title["title"])
    return titles    

parser = BeautifulSoup(html_content, "html.parser")
css_selector = "article.product_pod>h3>a"
print(get_titles(parser,css_selector))

