import requests
import os
from dotenv import load_dotenv
import datetime
import plotly.graph_objects as go


def get_timestamps(day_range):
    timestamps = []

    for day_delta in range(1, day_range + 1):
        delta_day = datetime.date.today() - datetime.timedelta(days=day_delta)

        timestamp_start = int(datetime.datetime(year=delta_day.year, month=delta_day.month,
                                                day=delta_day.day, tzinfo=datetime.timezone.utc).timestamp())
        seconds_for_day = 86399
        timestamp_end = timestamp_start + seconds_for_day

        timestamps.append((delta_day, timestamp_start, timestamp_end))

    return timestamps


def get_vk_mentions(vk_access_token, search_request, day_range):
    mentions = []
    url = 'https://api.vk.com/method/'
    method = 'newsfeed.search'
    timestamps = get_timestamps(day_range)

    payload = {'v': 5.122,
               'access_token': vk_access_token,
               'q': search_request,
               'count': 30}

    for timestamp in timestamps:
        timestamp_start = timestamp[1]
        timestamp_end = timestamp[2]

        payload.update({'start_time': timestamp_start,
                        'end_time': timestamp_end})

        response = requests.get(url + method, params=payload).json()
        if 'error' in response:
            raise requests.HTTPError(response['error'])
        mentions.append((timestamp[0], response['response']['total_count']))

    return mentions


def print_plot(vk_access_token, search_request, day_range):
    mentions = get_vk_mentions(vk_access_token, search_request, day_range)
    
    dates = []
    total_mentions = []

    for date, mention in mentions:
        dates.append(date)
        total_mentions.append(mention)

    fig = go.Figure([go.Bar(x=dates, y=total_mentions)])
    fig.show()


def main():
    load_dotenv()

    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    search_request = 'coca cola'
    day_range = 30

    print_plot(vk_access_token, search_request, day_range)


if __name__ == '__main__':
    main()
