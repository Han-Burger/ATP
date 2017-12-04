import plotly
import plotly.graph_objs as go
from atp.player.player import Player
from datetime import date, datetime
import os


def _players_rank_history(players, date_from, date_thru):
    """
    :param player:
    :param date_from: Can be None
    :param date_thru: Can be None
    :return: return Scatter
    """
    if not date_from: date_from = date(1900, 1, 1)
    if not date_thru: date_thru = date(9999, 12, 31)

    for player in players:
        df = player.rank_history
        mask = (df['date'] >= date_from) & (df['date'] <= date_thru)
        yield player.name, player.rank_history.loc[mask]


def plot_rank_history(players, date_from = None, date_thru = None):
    if not isinstance(players, list):
        players = [players]
    player_names = [p.name for p in players]
    file_name = '__'.join(player_names) + '.html'
    url = os.path.join(os.path.dirname(__file__), '../../data/plot', file_name)
    data = [
            go.Scatter(
                x = rank_history['date'],
                y = rank_history['singles_rank'],
                mode = 'lines+markers',
                name = name
            ) for name, rank_history in _players_rank_history(players, date_from, date_thru)]
    plotly.offline.plot(data, filename=url)


if __name__ == "__main__":
    names = ['Rafael Nadal', 'Roger Federer', 'Novak Djokovic', 'Andy Murray']
    players =[Player.build(name) for name in names]

    """
    df = players[0].rank_history
    mask = (df['date'] >= datetime.strptime('2010-1-1', '%Y-%m-%d').date()) \
           & (df['date'] <= datetime.strptime('2010-12-31', '%Y-%m-%d').date())
    print(df.loc[mask])
    """
    dates = [datetime.strptime(d, '%Y-%m-%d').date() for d in ('2007-01-01', '2018-01-01')]
    plot_rank_history(players, *dates)