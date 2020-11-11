#!/usr/bin/env python3
import requests, time
from bs4 import BeautifulSoup
from selenium import webdriver

# THIS FUNCTION GENERATES A URL FOR EACH PLAYER
def gen_player_link(search_player):
    url           = "https://www.basketball-reference.com/players/"
    html_list     = ["01.html", "02.html", "03.html", "04.html", "05.html"]
    search_player = search_player.lower()

    first = search_player.split()[0]
    last  = search_player.split()[1]

    first = first[:2]
    last  = last[0:5]
    last_init = last[0]

    url += last_init + "/"
    for i in html_list:
        player_tag = last + first + i
        tmp_url    = url + player_tag

        # check to see if name in the html == search_player
        if check_name(search_player, tmp_url) == True:
            url = tmp_url
            break 
    return url

# CHECK IF THE NAME IN THE HTML IS == TO THE DESIRED NAME
# OF THE PLAYER THE USER WANTS TO LOOK UP
# E.G. https://www.basketball-reference.com/players/d/davisan01.html
#           --> RETURNS THE PAGE FOR PLAYER 'Antonio Davis'
#      https://www.basketball-reference.com/players/d/davisan02.html
#           --> RETURNS THE PAGE FOR PLAYER 'Anthony Davis'
def check_name(player_name, link):
    r = requests.get(link)
    s = BeautifulSoup(r.content, 'lxml')
    for h1_tag in s.find_all('h1', attrs={"itemprop": "name"}):
        name = h1_tag.text
        name = name.strip()
        if name.lower() == player_name:
            return True
        else:
            return False


# GETS PLAYER STATS BASED ON THE YEAR
# 2020 IS SET AS THE DEFAULT YEAR   
def get_player_stats(URL, name, season='2020'):
    result = requests.get(URL)
    soup   = BeautifulSoup(result.content, 'lxml')

    # FORMAT FOR WHAT YEAR OF STATS TO GRAB
    per_game = "per_game."
    per_game += season
    
    # GET PLAYER STATS IN THEIR ASSOCIATED TAG(S)
    for tr_tag in soup.find_all('tr', id=per_game):
        age = tr_tag.find('td', attrs={"data-stat": "age"}).text
        ppg = tr_tag.find('td', attrs={"data-stat": "pts_per_g"}).text
        rb_per_g = tr_tag.find('td', attrs={"data-stat": "trb_per_g"}).text
        ast_per_g = tr_tag.find('td', attrs={"data-stat": "ast_per_g"}).text
        ft_pct = tr_tag.find('td', attrs={"data-stat": "ft_pct"}).text
        fg2_pct = tr_tag.find('td', attrs={"data-stat": "fg2_pct"}).text
        fg3_pct = tr_tag.find('td', attrs={"data-stat": "fg3_pct"}).text
        team = tr_tag.find('td', attrs={"data-stat": "team_id"}).text

        sep = "Player Stats " + name.upper() + "(" + season + ")"
        print("Player Stats %s (%s) " % (name.upper(), season ))
        print("*"*len(sep))
        print("team:   " + team)
        print("age:    " + age)
        print("ppg:    " + ppg)
        print("rpg:    " + rb_per_g)
        print("apg:    " + ast_per_g)
        print("fg2:   " + fg2_pct)
        print("fg3:   " + fg3_pct)
        print("ft:    " + ft_pct)

        player_dict = {'name': name, 'team': team, 'age': age, 
                       'ppg': ppg, 'rbg': rb_per_g,'apg': ast_per_g, 
                       'fg2': fg2_pct, 'fg3': fg3_pct, 'ft': ft_pct}
        return player_dict

'''
player = input("Enter player name: ")
year   = input("Enter year: ")
player_tag = gen_player_link(player)
URL = player_tag
print(URL)

result = requests.get(URL)
soup   = BeautifulSoup(result.content, 'lxml')

get_player_stats(URL, player, year)
'''