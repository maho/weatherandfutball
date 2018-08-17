import pytest

import weather

def test_weather_url():
    """ just run and check if it won't break """

    ret = weather.min_spread_day()
    assert ret == '14'

def wdata2url(data):
    content = 'ignored\n\n'
    
    for x, y, z in data:
        content += "%+6s%+6s%+6s\n" % (x, y, z)

    return "data:," + content


def test__fake_data():
    data = [(1, 3, 2),
            (2, 3, 3),  # min spread
            (3, 10, 2)]

    ret = weather.min_identifier(wdata2url(data), (0,6), (6,12), (12,18),
                                                ignrows=2)
    assert ret == '2'


def test_weather_empty_file():
    assert weather.min_identifier(wdata2url([]), (0,6), (6,12), (12,18),
                                  ignrows=2) == None


@pytest.mark.parametrize('eline', ['------------', ''])
def test_empty_line(eline):
    url = 'data:,header\n' + '\n'.join(3*[eline])
    assert weather.min_identifier(url, (0,2), (2,4), (4,6)) == None
