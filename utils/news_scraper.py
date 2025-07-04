from bs4 import BeautifulSoup
import requests

def get_ai_news():
    url = "https://www.analyticsvidhya.com/blog/category/artificial-intelligence/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    headlines = soup.select("h4.blog-title")
    return [h.text.strip() for h in headlines[:5]]
