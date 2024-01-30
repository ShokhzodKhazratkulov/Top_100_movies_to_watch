import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
contents = response.text
soup = BeautifulSoup(contents, "html.parser")

# print(soup.prettify())
lists = soup.find_all("h3", class_="title")
movie_titles = [movie.getText() for movie in lists[::-1]]
with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_titles:
        data = file.write(f"{movie}\n")



