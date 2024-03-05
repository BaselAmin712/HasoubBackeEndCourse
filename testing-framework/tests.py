# from assertionFunctions import *

# likes_dict = {"color": "blue", "fruit": "apple", "pet": "dog"}
# planets_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter',[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 'Saturn', 'Uranus', 'Neptune']

# if is_in_list(planets_list, 19):
#     print("was found")
# else:
#     print("not found")

import requests
from bs4 import BeautifulSoup

URL = "https://store.steampowered.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print(soup)