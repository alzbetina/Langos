from kinomaniak import Kinomaniak
import json

scraper_kinomaniak = Kinomaniak()
scraper_kinomaniak.scrape(2024)

with open("Kinomaniak.json", mode="w", encoding="utf-8") as kinomaniak_file:
    json.dump(scraper_kinomaniak.all_films, kinomaniak_file, ensure_ascii=False, indent=4)