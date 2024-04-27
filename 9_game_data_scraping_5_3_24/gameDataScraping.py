import re
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

URL = "https://store.steampowered.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

def upgrade_genre_counter(genre):
    if genre in genres_hist:
        genres_hist[genre] += 1
    else:
        genres_hist[genre] = 1


genres_hist = {}
games_by_name = {}

def get_games_names_and_genres(soup, games_by_name):
    popular_games_div = soup.find("div", id = "tab_upcoming_content")
    popular_games = popular_games_div.find_all("div", class_ = "tab_item_content")
    for game in popular_games:
        game_name = game.find("div", class_ = "tab_item_name").string
        game_genres = [re.sub(r'[^\w]', ' ', genre.string).strip() for genre in game.find("div", class_ = "tab_item_top_tags")]
        games_by_name.update({game_name: game_genres})
        for genre in game_genres:
            upgrade_genre_counter(genre)

get_games_names_and_genres(soup, games_by_name)

def print_genre_percentage(genre):
    if genre in genres_hist:
        games_number = len(games_by_name)
        print(round((genres_hist[genre] / games_number) * 100 , 2),"%")

print_genre_percentage("Music")

print(len(games_by_name))

def plot_tags(freq):
    plt.figure(figsize=(10, 6))
    plt.bar(freq.keys(), freq.values())
    plt.title('Top 10 Most Appeared Tags in Popular Games')
    plt.xlabel('Tag')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def pie_plot(per,genre):
    y = [per, 100-per]
    mylabels = [genre, 'other genres']
    plt.pie(y, labels = mylabels)
    plt.title('selected genre percentage')
    plt.show()

plot_tags(genres_hist)