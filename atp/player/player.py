from atp.webscraper.webscraper import parse_player_rank_history

class Player(object):
    def __init__(self, rank_history):
        """
        :param rank_history: a rank history dataframe
        """
        self.rank_history = rank_history

    @classmethod
    def from_webpage(cls, url):
        df = parse_player_rank_history(url)
        return cls(rank_history = df)

    @classmethod
    def from_local(cls, path):
        # TODO: read from pickle or csv
        pass


if __name__ == '__main__':
    url = r'http://www.atpworldtour.com/en/players/rafael-nadal/n409/rankings-history'
    rn = Player.from_webpage(url)
    print(rn.rank_history)