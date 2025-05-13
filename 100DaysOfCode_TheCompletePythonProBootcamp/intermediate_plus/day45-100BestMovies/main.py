import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# fetch html and save it within a variable
response = requests.get(url=URL)
movies = response.text

# get a list of movies' titles, using BeautifulSoup
soup = BeautifulSoup(movies, "html.parser")
raw_name = soup.find_all(name="h3")
clean_name = [name.getText() for name in raw_name]

# save movies in a file
for name in clean_name[::-1]:
    with open("movies.txt", "a") as file:
        file.write(f"{name}\n")
