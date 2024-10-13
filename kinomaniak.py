import re
import requests
from bs4 import BeautifulSoup

class Kinomaniak:
    def scrape(self, url: str) -> dict:
        movie_page = requests.get(url)
        soup = BeautifulSoup(movie_page.content, 'html.parser')


        information_table = soup.find("div", class_="card-body")
        movie_title = (information_table.find("h2", class_="h5")).text.strip()

        movie_elements = information_table.findAll("div", {"class": "col-8 col-xl-9 col-xxl-10"})
        information_dict = {
            "Movie Title": movie_title,
            "Premiere Czechia": movie_elements[0].text.strip(),
            "Distributor": movie_elements[1].text.strip(),
            "Country": movie_elements[2].text.strip(),
            "Premiere": movie_elements[3].text.strip(),
            "Studio": movie_elements[4].text.strip()}

        table_variable = ["Tržby v ČR \\($", "Návštěvnost v ČR", "1. víkend tržby","1. víkend diváci", "Víkendů v TOP 20", "Poměr diváků 1. víkend/celkem", "Přepočtené tržby akt. kurzem", "Vidělo lidí v ČR"]
        revenue_values = []

        revenue_table = soup.find("div", class_="col-12 col-xl-4 pt-4 pt-md-0")
        for variable in table_variable:
            revenue_elements = revenue_table.find(string=re.compile(variable))
            if revenue_elements is None:
                revenue_values.append("None")
                continue
            element = revenue_elements.parent.find_next("h3")
            clean_element = element.text.strip().replace('\xa0','')
            revenue_values.append(clean_element)

        revenue_keys = ["Total revenues", "Total viewers", "1st weekend revenues","1st weekend viewers", "TOP 20 weekends", "1st weekend/viewers", "Revenue in dollars", "Viewers/Population"]

        revenue_dict = dict(zip(revenue_keys,revenue_values))

        information_dict.update(revenue_dict)

        return information_dict
    

    def html_scrape(self, url: str):
        search_page = requests.get(url)
        soup = BeautifulSoup(search_page.content, 'html.parser')

        information_table = soup.find("table", class_="table table-hover table-bordered bg-white")
        film_url = []

        for link in information_table.find_all('a'):
            film_url.append(f'{"https://kinomaniak.cz"}{link.get("href")}')
        return film_url


    def films_urls(self, start_year):
        all_films = []

        for year in range(start_year, 2025):
            url_year = f"https://kinomaniak.cz/hledej/rozsirene/0/99/{year}/0/0/0"
            year_list = self.html_scrape(url_year)
            all_films.extend(year_list)
        return all_films
