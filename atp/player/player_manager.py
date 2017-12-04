from atp.player.player import Player
from atp.webscraper.webscraper import parse_player_rank_history, parse_singles_player_list
from urllib.parse import urljoin
from atp.logger.logger import Logger

logger = Logger('player_manager').get()

class PlayerManager(object):

    @staticmethod
    def load_player_statistics():
        player_list = parse_singles_player_list()
        atp_url = r'https://www.atpworldtour.com'
        players_rank_history =  {
                                    player_list.ix[i]['name']:
                                    parse_player_rank_history(urljoin(atp_url, player_list.ix[i]['ranking_history_link']))
                                    for i in range(len(player_list))
                                }
        print(players_rank_history)
        return players_rank_history

    @staticmethod
    def write_all_players_rank_history_to_file(format = 'csv'):

        func = {'csv': Player.write_player_rank_history_to_csv,
                'pickle': Player.write_player_rank_history_to_pickle}

        if format not in func:
            logger.warning("Write file type not supported.")

        player_list = parse_singles_player_list()
        atp_url = r'https://www.atpworldtour.com'
        for i in range(len(player_list)):
            player = Player.build_from_webpage(urljoin(atp_url, player_list.ix[i]['ranking_history_link']))
            func[format](player)


if __name__ == '__main__':
    PlayerManager.write_all_players_rank_history_to_file('csv')