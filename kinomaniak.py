import requests
from bs4 import BeautifulSoup

movie_page = requests.get('https://kinomaniak.cz/filmy/sladky-zivot-2024')
soup = BeautifulSoup(movie_page.content, 'html.parser')


information_table = soup.find("div", class_="card-body")
movie_title = (information_table.find("h2", class_="h5")).text.strip()

movie_elements = information_table.findAll("div", {"class": "col-8 col-xl-9 col-xxl-10"})
information_dict = {
    "Premiere Czechia": movie_elements[0].text.strip(),
    "Distributor": movie_elements[1].text.strip(),
    "Country": movie_elements[2].text.strip(),
    "Premiere": movie_elements[3].text.strip(),
    "Studio": movie_elements[4].text.strip()}



revenue_table = soup.find("div", class_="col-12 col-xl-4 pt-4 pt-md-0")
revenue_elements = revenue_table.findAll("h3", {"class": "h5"})

revenue_values = []
for element in revenue_elements:
    clean_element = element.text.strip().replace('\xa0',"")
    revenue_values.append(clean_element)

#print(revenue_elements[0].text.strip())
#print(revenue_values)
#print(movie_elements)

revenue_keys = ["Total revenues", "Total viewers", "1st weekend revenues","1st weekend viewers", "TOP 20 weekends", "1st weekend/viewers", "Revenue in dollars", "Viewers/Population"]
#revenue_values = revenue_elements.strip()
revenue_dict = dict(zip(revenue_keys,revenue_values))

information_dict.update(revenue_dict)


print(information_dict)