import random
from collections import namedtuple

Episode = namedtuple('Episode', 'title link pubdate show_id')
episode_data = {}


def display_results():
    # DISPLAY RESULTS
    start = random.randint(90, 110)
    latest_id = get_latest_show_id()
    end = random.randint(130, latest_id + 1)
    return end, start


def get_episode(show_id):
    # GET EPISODE
    info = episode_data.get(show_id)
    print("{}. {}".format(info.show_id, info.title))


def get_latest_show_id():
    latest_show_id = max(episode_data.keys())
    return latest_show_id


def show_header():
    # SHOW THE HEADER
    print("Welcome to the talk python info downloader.")
    print()