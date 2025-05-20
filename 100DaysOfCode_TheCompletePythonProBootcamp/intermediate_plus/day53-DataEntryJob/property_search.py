import requests
from bs4 import BeautifulSoup
import re

class PropertySearch:
    def __init__(self, link):
        self.link = link
        self.soup = self.fetch_site()
        self.links = []
        self.prices = []
        self.addresses = []
        self.create_links()
        self.create_prices()
        self.create_addresses()
        
    def fetch_site(self):
        response = requests.get(self.link)
        website = response.text
        soup = BeautifulSoup(website, "html.parser")
        return soup
    
    def create_links(self):
        all_links = self.soup.find_all(name="a", class_="property-card-link")
        for tag in all_links:
            self.links.append(tag.get("href"))
            
    def create_prices(self):
        all_prices = self.soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
        for tag in all_prices:
            match = re.search(r"^(\$[^+/]+)", tag.getText())
            self.prices.append(match.group(0))
            
    def create_addresses(self):
        all_addresses = self.soup.find_all(name="address")
        for address in all_addresses:
            self.addresses.append(address.getText().strip().replace("|", ""))
            
