import requests
import json
from vector_utils import Vector


def hex_to_int(s):
    s = s.lstrip('#')
    return [int(s[:2], 16), int(s[2:4], 16), int(s[4:6], 16)]


def get_json(url):
    response = requests.get(url)
    content = response.content.decode()
    data = json.loads(content)
    return data


def parse_colors(data_set):
    return dict((item['color'], hex_to_int(item['hex'])) for item in data_set['colors'])


if __name__ == '__main__':
    data_set_url = "https://raw.githubusercontent.com/dariusk/corpora/master/data/colors/xkcd.json"
    data_set = get_json(data_set_url)
    colors = parse_colors(data_set)

