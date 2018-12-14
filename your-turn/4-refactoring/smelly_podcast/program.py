from xml.etree import ElementTree

import requests

from service import Episode, episode_data, display_results, get_episode, get_latest_show_id, show_header


def main():
    show_header()

    # DOWNLOAD THE EPISODE DATA
    url = 'https://talkpython.fm/episodes/rss'

    resp = requests.get(url)
    resp.raise_for_status()

    dom = ElementTree.fromstring(resp.text)

    items = dom.findall('channel/item')
    episode_count = len(items)

    for idx, item in enumerate(items):
        episode = Episode(
            item.find('title').text,
            item.find('link').text,
            item.find('pubDate').text,
            episode_count - idx - 1
        )
        episode_data[episode.show_id] = episode

    # GET LATEST SHOW ID
    latest_show_id = get_latest_show_id()

    print("Working with total of {} episodes".format(latest_show_id))

    end, start = display_results()

    for show_id in range(start, end):
        get_episode(show_id)


if __name__ == '__main__':
    main()
