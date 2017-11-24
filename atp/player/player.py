from atp.webscraper.webscraper import parse_player_rank_history
import pandas as pd
import os
import pickle
import logging

class Player(object):
    def __init__(self, name, rank_history):
        """
        :param rank_history: a rank history dataframe
        """
        if (name is None):
            print ('Player Name cannot be None.')
        self.name = name
        self.rank_history = rank_history


    @staticmethod
    def name_to_path(name):
        return name.replace(' ', '_').lower()

    @classmethod
    def fill_in_df_name_path(cls, obj, name, path, file_type):
        if isinstance(obj, Player):
            name = obj.name
            obj = obj.rank_history
        name = name.lower().replace(' ', '_').replace('-', '_')
        if not path:
            # replace empty path or None path
            dirname = os.path.dirname
            folder_type = {'.csv': 'csv', '.pkl': 'pickle'}
            path = os.path.join(dirname(dirname(dirname(__file__))),
                                'data/' + folder_type[file_type] + '/' + name + file_type)
        return obj, name, path

    @classmethod
    def build_from_webpage(cls, url):
        return cls(*parse_player_rank_history(url))

    @classmethod
    def build_from_pickle(cls, name):
        file_name = cls.name_to_path(name) + '.pkl'
        dirname = os.path.dirname
        url = os.path.join(dirname(dirname(dirname(__file__))), 'data/pickle', file_name)
        obj = None
        if os.path.exists(url):
            with open(url, "rb") as f:
                while True:
                    try:
                        obj = pickle.load(f)
                    except EOFError:
                        return obj
        else:
            # logging.log('WARNING', 'Player file cannot find.')
            return None

    @classmethod
    def build_from_csv(cls, name):
        file_name = cls.name_to_path(name) + '.csv'
        dirname = os.path.dirname
        url = os.path.join(dirname(dirname(dirname(__file__))), 'data/csv', file_name)
        if os.path.exists(url):
            df = pd.read_csv(url)
            return cls(name, df)
        else:
            # logging.log('WARNING', 'Player file cannot find.')
            return None

    @classmethod
    def build(cls, name):
        obj = cls.build_from_pickle(name)
        if obj: return obj
        obj = cls.build_from_csv(name)
        if obj: return obj
        obj = cls.build_from_webpage()
        return cls.build_from_csv(name)

    @classmethod
    def write_player_rank_history_to_pickle(cls, obj, name = None, path = None):
        """
        :param obj: either a Player object or a player rank history df
        :param name: if obj is df, then need to provide the name of the player
        :param path: write path, default: /Atp/data/pickle/[player_name].pkl
        :return:
        """
        df, name, path = cls.fill_in_df_name_path(obj, name, path, '.pkl')
        with open(path, 'wb') as f:
            pickle.dump(obj, f)

    @classmethod
    def write_player_rank_history_to_csv(cls, obj, name = None, path = None):
        """
        :param obj: either a Player object or a player rank history df
        :param name: if obj is df, then need to provide the name of the player
        :param path: write path, default: /Atp/data/csv/[player_name].csv
        :return:
        """
        df, name, path = cls.fill_in_df_name_path(obj, name, path, '.csv')
        df.to_csv(path)



if __name__ == '__main__':
    # url = r'http://www.atpworldtour.com/en/players/rafael-nadal/n409/rankings-history'
    # rn = Player.build_from_webpage(url)
    # print(rn.rank_history)
    # Player.write_player_rank_history_to_pickle(rn)
    rn = Player.build('Roger Federer')
    print(rn.rank_history)