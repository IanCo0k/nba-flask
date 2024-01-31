from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to fetch the game log data for a player
def get_player_game_log(player_name):
    player_id = players.find_players_by_full_name(player_name)[0]['id']
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season=SeasonAll.all).get_data_frames()[0]
    return game_log


all_players = players.get_players()


@app.route('/', methods=['GET', 'POST'])
def index():
    game_log_data = None  # Initialize to None
    if request.method == 'POST':
        player_name = request.form['player_name']
        game_log_data = get_player_game_log(player_name)
    
    return render_template('game_log.html',player_name= player_name, game_log_data=game_log_data, all_players=all_players)

if __name__ == '__main__':
    app.run(debug=True)
