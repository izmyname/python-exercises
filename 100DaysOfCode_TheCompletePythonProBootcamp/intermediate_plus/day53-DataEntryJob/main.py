from property_search import PropertySearch
from google_form import GoogleForm

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLScL-xrOyWeRu9uVT0PQBaASfIrLGDY3xV1MeCH1EQIqh8hOdw/viewform?usp=header"
PROPERTY_SEARCH = "https://appbrewery.github.io/Zillow-Clone/"

            
property_search = PropertySearch(PROPERTY_SEARCH)   
fill_google = GoogleForm(GOOGLE_FORM)

for n in range(len(property_search.addresses)):
    fill_google.fill_form(property_search.addresses[n], property_search.prices[n], property_search.links[n])
