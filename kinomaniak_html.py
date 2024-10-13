import requests
from bs4 import BeautifulSoup

class Kinomaniak:
    def html_scrape(url: str):
        search_page = requests.get(url)
        soup = BeautifulSoup(search_page.content, 'html.parser')

        information_table = soup.find("table", class_="table table-hover table-bordered bg-white")
        film_url = []

        for link in information_table.find_all('a'):
            film_url.append(f'{"https://kinomaniak.cz"}{link.get("href")}')
        return film_url

    def films_urls(start_year, url_part1, url_part2):
        all_films = []

        for year in range(2010, 2025):
            url_year = url_part1 + str(start_year) + url_part2
            year_list = html_scrape(url_year)
            all_films.extend(year_list)
            start_year += 1
        return all_films
