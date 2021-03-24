from bs4 import BeautifulSoup
import requests
from db import *


my_data = []
html_text = requests.get('https://store.steampowered.com/search/?sort_by=Released_DESC&supportedlang=french&category1=998&os=win').text
soup = BeautifulSoup(html_text, 'lxml')
games = soup.find_all('a', class_ = "search_result_row")

for game in games:   
    game_img_src = game.find('img')['src']
    game_name = game.find('span', class_ = "title").text
    game_release_date = game.find('div', class_ = "search_released").text
    my_data.append((game_img_src, game_name, game_release_date))
    # print(f'''
    # game image : {game_img_src},
    # game name : {game_name}, 
    # game release_date : {game_release_date}, 
    # ''')
# print("games = ",my_data)
my_data.reverse()
print("games = ",my_data)
# cur.execute("DROP TABLE IF EXISTS games")
cur.execute("DROP TABLE IF EXISTS games")
cur.execute("CREATE TABLE  games (id SERIAL PRIMARY KEY, img_src VARCHAR(255), name VARCHAR(255), release_date VARCHAR(255))")

def insert_games(value_data):
    sql = "INSERT INTO games (img_src, name, release_date) VALUES (%s, %s, %s)"
    val = value_data
    cur.executemany(sql, val)
    conn.commit()
    print(cur.rowcount, "record inserted.")

insert_games(my_data)