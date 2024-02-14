from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguestandingsv3
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playercareerbycollege
from nba_api.stats.endpoints import playerawards
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import SeasonAll
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to fetch the game log data for a player
def get_player_game_log(player_name):
    player_id = players.find_players_by_full_name(player_name)[0]['id']
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season=SeasonAll.all).get_data_frames()[0]
    return game_log

def get_player_career_stats(player_name):
    player_id = players.find_players_by_full_name(player_name)[0]['id']
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id).get_data_frames()[0]
    return career_stats

def get_player_by_college(college_name):
    college = playercareerbycollege.PlayerCareerByCollege(college=college_name).get_data_frames()[0]
    return college

def get_season_standings(season):
    standings = leaguestandingsv3.LeagueStandingsV3(season=season).get_data_frames()[0]
    return standings

def get_player_awards(player_name):
    player_id = players.find_players_by_full_name(player_name)[0]['id']
    awards = playerawards.PlayerAwards(player_id=player_id).get_data_frames()[0]
    return awards

def get_games_by_player(player_name):
    player_id = players.find_players_by_full_name(player_name)[0]['id']
    games = leaguegamefinder.LeagueGameFinder(player_id_nullable=player_id).get_data_frames()[0]
    return games



all_players = players.get_players()


@app.route('/game-log', methods=['GET', 'POST'])
def index():
    game_log_data = None  # Initialize to None
    player_name = ''
    if request.method == 'POST':
        player_name = request.form['player_name']
        game_log_data = get_player_game_log(player_name).head(10)  # Get the last 10 games
    
    return render_template('game_log.html',player_name= player_name, game_log_data=game_log_data, all_players=all_players)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/career', methods=['GET', 'POST'])
def career_stats():
    career_stats_data = None
    player_name = ''
    if request.method == 'POST':
        player_name = request.form['player_name']
        career_stats_data = get_player_career_stats(player_name)
    return render_template('career.html', player_name=player_name, career_stats_data=career_stats_data, all_players=all_players)


if __name__ == '__main__':
    app.run(debug=True)
