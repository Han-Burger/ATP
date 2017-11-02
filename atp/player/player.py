from atp.webscraper.webscraper import parse_player_rank_history
import pandas as pd
import os
import pickle

class Player(object):
    def __init__(self, name, rank_history):
        """
        :param rank_history: a rank history dataframe
        """
        if (name is None):
            print ('Player Name cannot be None.')
        self.name = name
        self.rank_history = rank_history

    @classmethod
    def build_from_webpage(cls, url):
        return cls(*parse_player_rank_history(url))

    @classmethod
    def build_from_pickle(cls, path):
        # TODO: read from pickle or csv
        pass

    @classmethod
    def build_from_csv(cls, path):
        pass

    @classmethod
    def build(cls):
        pass

    @classmethod
    def write_player_rank_history_to_pickle(cls, obj, name = None, path = None):
        """
        :param obj: either a Player object or a player rank history df
        :param name: if obj is df, then need to provide the name of the player
        :param path: write path, default: /Atp/data/pickle/[player_name].pkl
        :return:
        """
        df, name, path = cls.fill_in_df_and_name(obj, name, path, '.pkl')
        with open(path, 'wb') as f:
            pickle.dump(obj, f)

    @classmethod
    def write_player_rank_history_to_csv(cls, obj, name = None, path = None):
        """
        :param obj: either a Player object or a player rank history df
        :param name: if obj is df, then need to provide the name of the player
        :param path: write path, default: /Atp/data/pickle/[player_name].pkl
        :return:
        """
        df, name, path = cls.fill_in_df_and_name(obj, name, path, '.csv')
        with open(path, 'wb') as f:
            pickle.dump(obj, f)

    @classmethod
    def fill_in_df_and_name(cls, obj, name, path, file_type):
        if isinstance(obj, Player):
            name = obj.name
            obj = obj.rank_history
        name = name.lower().replace(' ', '_').replace('-', '_')
        if not path:
            # replace empty path or None path
            dirname = os.path.dirname
            path = os.path.join(dirname(dirname(dirname(__file__))), 'data/pickle/' + name + file_type)
        return obj, name, path


if __name__ == '__main__':
    url = r'http://www.atpworldtour.com/en/players/rafael-nadal/n409/rankings-history'
    rn = Player.build_from_webpage(url)
    print(rn.rank_history)
    Player.write_player_rank_history_to_pickle(rn)