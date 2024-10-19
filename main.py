from kinomaniak import Kinomaniak
from kinomaniak_sk import Kinomaniak_SK
from CSFD import CSFD
import json

scraper_kinomaniak = Kinomaniak()
scraper_kinomaniak.scrape(2024)

scraper_kinomaniak_sk = Kinomaniak_SK()
scraper_kinomaniak_sk.scrape(2011)

scraper_CSFD = CSFD()
scraper_CSFD.scrape(1)

with open("Kinomaniak.json", mode="w", encoding="utf-8") as kinomaniak_file:
    json.dump(scraper_kinomaniak.all_films, kinomaniak_file, ensure_ascii=False, indent=4)

with open("Kinomaniak_sk.json", mode="w", encoding="utf-8") as kinomaniak_file_sk:
    json.dump(scraper_kinomaniak_sk.all_films, kinomaniak_file_sk, ensure_ascii=False, indent=4)

with open("CSFD.json", mode="w", encoding="utf-8") as CSFD_file:
    json.dump(scraper_CSFD.all_films, CSFD_file, ensure_ascii=False, indent=4)
