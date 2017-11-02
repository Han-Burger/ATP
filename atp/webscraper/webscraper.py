import requests
from bs4 import BeautifulSoup
from atp.webscraper.util import parse_rank_table, load_header
import pandas as pd
import os
rank_history_header = load_header(os.path.join(os.path.dirname(__file__), 'rank_history_df.json'))
player_list_header = load_header(os.path.join(os.path.dirname(__file__), 'player_list_df.json'))



def parse_player_rank_history(url):
    """
    :param url: atp player raking history page url
    :return:
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    rs = soup.find('div', attrs = {'id': 'playerRankHistoryContainer'})
    tb = rs.find('tbody').find_all('tr')
    mat = [[parse_rank_table(d.text.strip()) for d in row.find_all('td')] for row in tb]
    name = url.split('/')[-3].replace('-', ' ').title()
    return name, pd.DataFrame.from_records(mat, columns = rank_history_header)



def parse_singles_player_list(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    rs = soup.find('div', attrs={'id': 'rankingDetailAjaxContainer'})
    tb = rs.find('tbody').find_all('tr')
    mat = [[d.text, d['href'], '/'.join(d['href'].split('/')[:-1] + ['rankings-history'])]
           for row in tb for d in row.find('td', attrs = {'class': 'player-cell'}).find_all('a')]
    return pd.DataFrame.from_records(mat, columns = player_list_header)


if __name__ == '__main__':
    # url = r'http://www.atpworldtour.com/en/players/rafael-nadal/n409/rankings-history'
    # print (parse_player_rank_history(url))

    url = r'https://www.atpworldtour.com/en/rankings/singles'
    player_list = parse_singles_player_list(url)
    atp_url = r'https://www.atpworldtour.com'
    name, df = parse_player_rank_history(atp_url + player_list['ranking_history_link'][0])
    print(df)
    print(name)
