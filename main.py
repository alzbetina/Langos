from kinomaniak import Kinomaniak

scraper_kinomaniak = Kinomaniak()
scraper_kinomaniak.scrape(2024)
print(scraper_kinomaniak.all_films)