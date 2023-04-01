from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.naturalslim.app/food")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup)
articles = soup.find_all(name="h4")
print(articles)