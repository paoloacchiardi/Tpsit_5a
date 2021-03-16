#What is the highest rated game by Electronic Arts?, site -> https://rawg.io/apidocs#use-cases, run this by Anaconda Prompt
import requests as rq

url = "https://api.rawg.io/api/developers"
parameters = {'search' : 'Electronic%20Arts', 'page_size' : '1'}
values = rq.get(url = url, params = parameters)
results = values.json()["results"]
id = results[0]["id"] # id EA -> 109
url = "https://api.rawg.io/api/games"
parameters = {'ordering' : '-rating', 'developers' : id}
values = rq.get(url = url, params = parameters)
data = values.json()["results"]
top_game_name = data[0]["name"]
top_game_rating = data[0]["rating"]
max_rating = data[0]["rating_top"]
print(f"Highest rated game by Electronic Arts:\nName -> {top_game_name}\nRating -> {top_game_rating}/{max_rating}")