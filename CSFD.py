import requests
import re
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

    def scrape_film(self, url: str) -> dict:   
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
        movie_page = requests.get(url, headers=headers)
        soup = BeautifulSoup(movie_page.content, 'html.parser')
    
        info = soup.find("div", class_="film-info")
    
        inforating = soup.find("div", class_="box-rating box-rating-withtabs")
    
        table_variable = ["Režie", "Předloha", "Scénář", "Kamera", "Hudba"]
    
        contributor_list = []
        actors_list = []
    
        #základní údaje
        title = info.find("h1").text.strip()
        genre = info.find("div", class_="genres").text
        origin_raw = info.find("div", class_="origin").text
        origin_clean = re.sub(r'\s+', '', origin_raw)
    
        #hledání režie, předlohy, scénáře, atd.
        for variable in table_variable:
            element = info.find("h4", string=re.compile(variable))
            if element is None:
                contributor_list.append(None)
                continue
            new_element = element.find_next("a").text
            contributor_list.append(new_element)
    
        #zvlášť loop pro herce včetně hidden údajů
        actors_parent = info.find(string=re.compile("Hrají"))
        actors_siblings = actors_parent.parent.findNextSiblings("a")
        for sibling in actors_siblings:
            actor = sibling.text
            actors_list.append(actor)
        hidden_actor = actors_parent.find_next("span").findAll("a")
        for hidden in hidden_actor:
            actor = hidden.text.strip()
            actors_list.append(actor)
    
        #hodnocení v % a počet hodnocení
        rating = inforating.find("div", class_="film-rating-average").text.strip()
        rates_parent = inforating.find(string=re.compile("Hodnocení"))
        rates = rates_parent.parent.find_next("span").text.replace("(","").replace(")","").replace("\xa0","")
    
    
        #dictionary keys
        film_keys = ["Movie Title", "Rating", "Number of Rates", "Genre", "Origin", "Actors"]
        film_values = [title, rating, rates, genre, origin_clean, actors_list]
        film_dictionary = dict(zip(film_keys, film_values))
    
        contributor_keys = ["Director", "Based on", "Screenplay", "Cinematography", "Score"]
        contributor_dict = dict(zip(contributor_keys, contributor_list))
    
        film_dictionary.update(contributor_dict)
    
        return film_dictionary
