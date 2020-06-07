import requests
import json
from vector_utils import Vector as vec

from mpl_toolkits import mplot3d
import numpy as np 
import matplotlib.pyplot as plt

def get_content(url):
    response = requests.get(url)
    content = response.content.decode()
    return content


def get_json(url):
    content = get_content(url)
    data = json.loads(content)
    return data


def hex_to_rgb(s):
    s = s.lstrip('#')
    return [int(s[:2], 16), int(s[2:4], 16), int(s[4:6], 16)]


def parse_colors(data_set):
    return dict((item['color'], hex_to_rgb(item['hex'])) for item in data_set['colors'])


def closest(space, coord, n=10):
    return sorted(space.keys(), key=lambda x: vec.distance(space[x], coord))[:n]


if __name__ == '__main__':
    data_set_url = "https://raw.githubusercontent.com/dariusk/corpora/master/data/colors/xkcd.json"
    data_set = get_json(data_set_url)
    colors = parse_colors(data_set)

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    plt.show(fig)

