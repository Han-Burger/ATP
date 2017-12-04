from atp.player.player import Player
from atp.webscraper.webscraper import parse_player_rank_history, parse_singles_player_list
from urllib.parse import urljoin
from atp.logger.logger import Logger
from atp.util.singleton_meta import Singleton
logger = Logger('player_manager').get()

class PlayerManager(object, metaclass=Singleton):
    ...

if __name__ == '__main__':
    ...
    # PlayerManager.write_all_players_rank_history_to_file('csv')