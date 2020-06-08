import requests
import json
from vector_utils import Vector as vec
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import math

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


def calculate_size(dist):
    pass


def closest(colors, to, n):
    closest_colors = ((c, vec.distance(to, c)) for c in colors.values())
    return sorted(closest_colors, key=lambda c: c[1])[:n]


def plot_data(ax, values, colors, sizes):
    xdata, ydata, zdata = zip(*values)
    ax.scatter3D(xdata, ydata, zdata, c=colors /
                 255.0, s=sizes, depthshade=False)


def plot_closest(ax, colors, to):
    distances = closest(colors, to, n=len(colors)//2)
    max_distance = max(distances, key=lambda x: x[1])[1]
    sizes = np.array(
        list(map(lambda x: (math.log2(max_distance + 1) - math.log2(x[1] + 1))*100, distances)))
    rgb_values = list(map(lambda x: x[0], distances))
    plot_data(ax, rgb_values, np.array(rgb_values), sizes)


def init_projection(size=(13, 10)):
    plt.figure(figsize=size, dpi=90)
    ax = plt.axes(projection='3d')
    ax.set_axis_off()
    return ax


def print_colors(colors):
    print("\n-----COLOR LIST-----")
    for color in colors.keys():
        print(color)


if __name__ == '__main__':
    data_set_url = "https://raw.githubusercontent.com/dariusk/corpora/master/data/colors/xkcd.json"
    data_set = get_json(data_set_url)
    colors = parse_colors(data_set)

    print_colors(colors)

    color = input(
        "\nEnter a color from the color list or just enter an hexadecimal value: ")
    
    if color in colors:
        color = colors[color]
    else:
        color = hex_to_rgb(color)
        
    ax = init_projection()
    plot_closest(ax, colors, color)
    plt.show()

