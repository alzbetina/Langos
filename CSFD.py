import requests
from bs4 import BeautifulSoup

page_start = 1


class CSFD:
    def scrape_film_CSFD(self, page_start):
        self.all_films_url = []

        for page in range(page_start, 8):
            url_page = f'https://www.csfd.cz/podrobne-vyhledavani/?page={page}&searchParams=rlW0rKOyVwcoZS0fVzqyoaWyVwc7VwRvBygqYPVlVwcoKFjvZlV6JmxfZGIqYPV0VwcoZljkZljkAPjlZljkZvjmZS0fVaE5pTHvBwA9YPWipzyanJ4vBafvZFV6J10fVwVvByfkKFjvZlV6J10fVwDvByf2APjkAmWqYPW0rKOyVwblsFjvrJIupy9zpz9gVwblZQRjYPW5MJSlK3EiVwblZQV0YPWlLKEcozqsMaWioFV6oaIfoPjvpzS0nJ5aK3EiVwchqJkfYPW0LJpvBygqYPWuL3EipvV6J10fVzEcpzIwqT9lVwcoKFjvL29gpT9mMKVvBygqYPWmL3WyMJ53pzy0MKVvBygqYPWuqKEbo3VvBygqYPWwnJ5yoJS0o2qlLKObMKVvBygqYPWjpz9xqJA0nJ9hVwcoKFjvL2SmqTyhMlV6J10fVzIxnKDvBygqYPWmo3IhMPV6J10fVaAwMJ5iM3WupTu5VwcoKFjvoJSmnlV6J10fVzAip3E1oJImVwcoKFjvL29hMTy0nJ9hplV6J119'
            page_list = self.scrape_films_page(url_page)
            self.all_films_url.extend(page_list)
        
    
    def scrape_films_page(self, url: str):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
        search_page = requests.get(url, headers=headers)
        soup = BeautifulSoup(search_page.content, 'html.parser')

        information_table = soup.find("table", class_="striped")
        film_url = []

        for link in information_table.find_all('a'):
            film_url.append(f'{"https://www.csfd.cz"}{link.get("href")}')
        return film_url
