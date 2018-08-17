import pytest

import weather

def test_weather_url():
    """ just run and check if it won't break """

    ret = weather.min_spread_day()
    assert isinstance(ret, str)

def data2url(data):
    content = "ignored header\n\n"
    for x, y, z in data:
        content += "%+6s%+6s%+6s\n" % (x, y, z)

    return "data:," + content


def test_weather_fake_data(monkeypatch):
    data = [(1, 3, 2),
            (2, 3, 3),  # min spread
            (3, 10, 2)]

    monkeypatch.setattr(weather, 'URL', data2url(data))

    assert weather.min_spread_day() == '2'


def test_weather_empty_file(monkeypatch):
    monkeypatch.setattr(weather, 'URL', data2url([]))

    assert weather.min_spread_day() == None
