from threading import Thread
from atp.util.singleton_meta import Singleton
from atp.logger.logger import Logger
from atp.player.player import Player
from atp.webscraper.webscraper import parse_player_rank_history, parse_singles_player_list
from urllib.parse import urljoin

logger = Logger("PlayerDataDownloader").get()

class PlayerDataDownloadThread(Thread):

    func = {'csv': Player.write_player_rank_history_to_csv,
            'pickle': Player.write_player_rank_history_to_pickle}

    def __init__(self, url, format):
        super().__init__()
        self.download_url = url
        self.format = format

    def run(self):
        logger.info('Start downloading from: ' + self.download_url)
        player = Player.build_from_webpage(self.download_url)
        __class__.func[self.format](player)
        logger.info('Complete downloading from: ' + self.download_url)



class PlayerDataDownloader(object, metaclass=Singleton):

    def load_player_statistics(self):
        player_list = parse_singles_player_list()
        atp_url = r'https://www.atpworldtour.com'
        players_rank_history =  {
                                    player_list.ix[i]['name']:
                                    parse_player_rank_history(urljoin(atp_url, player_list.ix[i]['ranking_history_link']))
                                    for i in range(len(player_list))
                                }
        print(players_rank_history)
        return players_rank_history


    def write_all_players_rank_history_to_file(self, format = 'csv'):

        if format not in ('csv', 'pickle'):
            logger.warning("Write file type not supported.")

        player_list = parse_singles_player_list()
        atp_url = r'https://www.atpworldtour.com'

        thread_list = []
        for i in range(len(player_list)):
            download_url = urljoin(atp_url, player_list.ix[i]['ranking_history_link'])
            thread_list.append(PlayerDataDownloadThread(download_url, format))

        for thread in thread_list: thread.start()
        for thread in thread_list: thread.join()
        logger.info("Complete downloading player ranking history.")



if __name__ == "__main__":
    PlayerDataDownloader().write_all_players_rank_history_to_file('pickle')


