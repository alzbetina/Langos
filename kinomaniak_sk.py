import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Kinomaniak_SK:
    def scrape (self, start_year):
        self.scrape_film_list(start_year)
        self.all_films = []
        for film_url in self.all_films_url:
            film = self.scrape_film(film_url)
            self.all_films.append(film)

    def scrape_film(self, url: str) -> dict:
        movie_page = requests.get(url)
        soup = BeautifulSoup(movie_page.content, 'html.parser')

        information_dict = {}

        information_table = soup.find("div", class_="card-body")
        movie_title = soup.find("h1", string=re.compile(".* - Tržby a návštěvnost")).text.strip()
        movie_title = movie_title.replace(" - Tržby a návštěvnost", "")

        information_dict["Movie Title"] = movie_title

        table_details = ["Start ČR", "Distribuce", "Země", "Premiéra", "Studio"]
        movie_values = []

        for detail in table_details:
            movie_elements = information_table.find(string=re.compile(detail))
            if movie_elements is None:
                movie_values.append(None)
                continue
            element = movie_elements.find_next("div").find("a")  
            clean_element = element.text.strip()
            movie_values.append(clean_element)
        
        movie_keys = ["Premiere Czechia", "Distributor", "Country","Premiere", "Studio"]

        movie_dict = dict(zip(movie_keys, movie_values))

        information_dict.update(movie_dict)


        table_variable = ["Tržby v ČR \\(hrubé\\)", "Návštěvnost v ČR", "1. víkend tržby","1. víkend diváci", "Víkendů v TOP 20", "Poměr diváků 1. víkend/celkem", "Přepočtené tržby akt. kurzem", "Vidělo lidí v ČR"]
        revenue_values = []

        revenue_table = soup.find("div", class_="col-12 col-xl-4 pt-4 pt-md-0")
        for variable in table_variable:
            revenue_elements = revenue_table.find(string=re.compile(variable))
            if revenue_elements is None:
                revenue_values.append(None)
                continue
            element = revenue_elements.parent.find_next("h3")
            clean_element = element.text.strip().replace('\xa0','')
            revenue_values.append(clean_element)

        revenue_keys = ["Total revenues", "Total viewers", "1st weekend revenues","1st weekend viewers", "TOP 20 weekends", "1st weekend/viewers", "Revenue in dollars", "Viewers/Population"]

        revenue_dict = dict(zip(revenue_keys,revenue_values))

        information_dict.update(revenue_dict)

        return information_dict
    

    def scrape_films_page(self, url: str):
        search_page = requests.get(url)
        soup = BeautifulSoup(search_page.content, 'html.parser')

        information_table = soup.find("table", class_="table table-hover table-bordered bg-white")
        film_url = []

        for link in information_table.find_all('a'):
            film_url.append(f'{"https://kinomaniak.cz"}{link.get("href")}')
        return film_url


    def scrape_film_list(self, start_year):
        self.all_films_url = []

        for year in range(start_year, datetime.now().year + 1):
            url_year = f"https://kinomaniak.cz/hledej/rozsirene/0/169/{year}/0/0/0"
            year_list = self.scrape_films_page(url_year)
            self.all_films_url.extend(year_list)
        