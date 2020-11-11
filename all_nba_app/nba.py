#!/usr/bin/env python3
from nba_api.stats import endpoints
from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import commonplayerinfo
from urllib import parse as urlparse
import pandas as pd
import numpy as np
import os


nba_teams_dict = {}
# sets nba_teams_dict
def init_teams():
    nba_teams = teams.get_teams()
    i = 1
    for t in nba_teams:
        nba_teams_dict[i] = t['nickname']
        i += 1
    print(nba_teams_dict)

# ['LeagueID', 'SeasonID', 'TeamID', 'TeamCity', 'TeamName', 'Conference', 'ConferenceRecord', 'PlayoffRank', 'ClinchIndicator', 'Division', 'DivisionRecord', 'DivisionRank', 'WINS', 'LOSSES', 'WinPCT', 'LeagueRank', 'Record', 'HOME', 'ROAD', 'L10', 'Last10Home', 'Last10Road', 'OT', 'ThreePTSOrLess', 'TenPTSOrMore', 'LongHomeStreak', 'strLongHomeStreak', 'LongRoadStreak', 'strLongRoadStreak', 'LongWinStreak', 'LongLossStreak', 'CurrentHomeStreak', 'strCurrentHomeStreak', 'CurrentRoadStreak', 'strCurrentRoadStreak', 'CurrentStreak', 'strCurrentStreak', 'ConferenceGamesBack', 'DivisionGamesBack', 'ClinchedConferenceTitle', 'ClinchedDivisionTitle', 'ClinchedPlayoffBirth', 'EliminatedConference', 'EliminatedDivision', 'AheadAtHalf', 'BehindAtHalf', 'TiedAtHalf', 'AheadAtThird', 'BehindAtThird', 'TiedAtThird', 'Score100PTS', 'OppScore100PTS', 'OppOver500', 'LeadInFGPCT', 'LeadInReb', 'FewerTurnovers', 'PointsPG', 'OppPointsPG', 'DiffPointsPG', 'vsEast', 'vsAtlantic', 'vsCentral', 'vsSoutheast', 'vsWest', 'vsNorthwest', 'vsPacific', 'vsSouthwest', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'PreAS', 'PostAS']
def get_standings():
    data    = endpoints.leaguestandings.LeagueStandings(season='2019-20')
    d_frame = data.standings.get_data_frame()
    print(d_frame.loc[0: ,['TeamName', 'Conference', 'Record', 'HOME', 'ROAD', ]].to_string(col_space=15, index=False, justify='left'))

# league leaders endpoint
# PARAMETERS: https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/leagueleaders.md
def lg_leaders():
    data    = endpoints.leagueleaders.LeagueLeaders(season='2019-20')
    d_frame = data.league_leaders.get_data_frame()

    # PRINT TABLE
    print(d_frame.loc[0:9, ['RANK', 'PLAYER', 'TEAM', 'GP', 'PTS', 'FG_PCT', 'FG3_PCT', \
                    'FT_PCT', 'REB', 'AST', 'STL', 'TOV'] ].to_string(col_space=8, index=False, justify='parent') )


# player = { 'id': player_id, 'full_name': full_name, 'first_name': first_name, 'last_name': last_name, 'is_active': True or False }
def pick_player(player):
    for p in players.get_players():
        name = p['full_name']
        if name.lower() == player.lower():
            ret = p
    return ret['id']

# players stats for must recent season
def player_stats(id):
    data    = endpoints.playercareerstats.PlayerCareerStats(id)
    d_frame = data.season_totals_regular_season.get_data_frame()
    #stats   = d_frame.loc[d_frame['SEASON_ID'] == '2019-20']
    stats = d_frame.tail(1)

    player_age  = stats['PLAYER_AGE']
    player_team = stats['TEAM_ABBREVIATION']
    season      = stats['SEASON_ID']
    gp          = stats['GP']
    gs          = stats['GS']
    fg_pct      = stats['FG_PCT']
    fg3_pct     = stats['FG3_PCT']
    ft_pct      = stats['FT_PCT']
    ppg         = str(round( int(stats['PTS'])/int(gp) * 10 ) / 10)
    rpg         = str(round( int(stats['REB'])/int(gp) * 10 ) / 10)
    apg         = str(round( int(stats['AST'])/int(gp) * 10 ) / 10)

    table = pd.DataFrame({
                        'PLAYER': player,'TEAM': player_team, 'SEASON': season,'GP': gp, 'GS': gs, 'PPG': ppg, 'RPG': rpg, 'APG': apg,'FG%': fg_pct, '3P%': fg3_pct, 'FT%': ft_pct
                        })

    print(table.to_string(col_space=5, index=False))


#init_teams()
get_standings()
lg_leaders()

#player = input("Enter Player Name: ")
#player = "kevin durant"
#tmp    = pick_player(player)
#player_stats(tmp)
"""
my_str = "Please select on of the following options:\n-----------------------------------------\n" \
    + "1. Show League Leaders\n" \
    + "2. Show Current Standings\n" \
    + "3. Select Player\n"
choice = input(my_str)

if(choice != "1" or "2" or "3"):
    print("Please enter a valid input")

if choice == "2":
    os.system('clear')
    get_standings()

if choice == "3":
    os.system('clear')
    player = input("Enter player name: ") 
    player = player.lower()
    tmp    = pick_player(player)
    player_stats(tmp)
"""    
for keys in nba_teams_dict:
    print("%-2d: %s" % ( keys, nba_teams_dict.get(keys) ))
