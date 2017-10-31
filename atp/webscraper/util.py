from datetime import datetime
import json
import re

def parse_date(str):
    return datetime.strptime(str, '%Y.%m.%d').date()

def parse_rank(str):
    return int(re.search(r'\d+', str).group())

def parse_rank_table(str):
    dateformat = r'^\d{4}\.\d{1,2}\.\d{1,2}$'
    return parse_date(str) if re.match(dateformat, str) else parse_rank(str)

def load_header(url):
    with open(url) as data_file:
        data = json.load(data_file)
    return data
