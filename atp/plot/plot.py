import plotly
from atp.player.player import Player

def plot_rank_history(player, time_from = None, time_to = None):
    py.offline.iplot(data, filename='rafa rank history')


if __name__ == "__main__":
    rn = Player.build('Rafael Nadal')
    df = rn.rank_history

    import plotly.plotly as py
    import plotly.graph_objs as go

    data = [go.Scatter(x=df['date'], y=df['singles_rank'])]
    py.iplot(data, filename='rafa rank history')
    # py.offline.iplot()