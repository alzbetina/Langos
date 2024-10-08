from kinomaniak import Kinomaniak

scraper_kinomaniak = Kinomaniak()
url1 = "https://kinomaniak.cz/filmy/sladky-zivot-2024"
data_film1 = scraper_kinomaniak.scrape(url1)
print(data_film1)
url2 = "https://kinomaniak.cz/filmy/tankovy-prapor"
data_film2 = scraper_kinomaniak.scrape(url2)
print(data_film2)
