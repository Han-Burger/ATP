from atp.player.player import Player
from atp.webscraper.webscraper import parse_player_rank_history, parse_singles_player_list

class PlayerManager(object):

    @staticmethod
    def load_player_statistics():
        url = r'https://www.atpworldtour.com/en/rankings/singles'
        player_list = parse_singles_player_list(url)
        atp_url = r'https://www.atpworldtour.com'
        players_rank_history =  {
                                    player_list.ix[i]['name']:
                                    parse_player_rank_history(atp_url + player_list.ix[i]['ranking_history_link'])
                                    for i in range(len(player_list))
                                }
        print(players_rank_history)
        return players_rank_history


if __name__ == '__main__':
    PlayerManager.load_player_statistics()