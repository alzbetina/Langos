from kinomaniak import Kinomaniak
from kinomaniak_html import Kinomaniak

start_year = 2010
url_part1 = "https://kinomaniak.cz/hledej/rozsirene/0/99/"
url_part2 = "/0/0/0"

html_data = scraper_kinomaniak.films_urls(start_year, url_part1, url_part2)

scraper_kinomaniak = Kinomaniak()
url1 = "https://kinomaniak.cz/filmy/sladky-zivot-2024"
data_film1 = scraper_kinomaniak.scrape(url1)
print(data_film1)
url2 = "https://kinomaniak.cz/filmy/tankovy-prapor"
data_film2 = scraper_kinomaniak.scrape(url2)
print(data_film2)

url_list = scraper_kinomaniak.films_urls(2010)
print(url_list)
