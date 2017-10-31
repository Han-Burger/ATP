import requests
from bs4 import BeautifulSoup
from util import parse_table, load_header
import json
import pandas as pd
rank_history_header = load_header('rank_history_df.json')


def player_rank_history_parser(url):
    """
    :param url: atp player raking history page url
    :return:
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    rs = soup.find('div', attrs={'id': 'playerRankHistoryContainer'})
    tb = rs.find('tbody').find_all('tr')
    mat = [[parse_table(d.text.strip()) for d in row.find_all('td')] for row in tb]
    return pd.DataFrame.from_records(mat, columns = rank_history_header)



if __name__ == '__main__':
    url = r'http://www.atpworldtour.com/en/players/rafael-nadal/n409/rankings-history'
    print (player_rank_history_parser(url))
