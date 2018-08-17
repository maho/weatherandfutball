import csv
from urllib.request import urlopen

URL="http://codekata.com/data/04/weather.dat"

def val(b):
    return float(b.strip().replace(b"*", b""))

def min_spread_day():
    data = []
    with urlopen(URL) as request:
        # ignore 2 header and empty line
        request.readline()
        request.readline()

        for line in request:
            day = line[:6].strip()
            if day == b'mo':
                break  # last line, ignored

            maxt = val(line[6:12])
            mint = val(line[12:18])

            data.append((day.decode(), maxt - mint))

    if not data:
        return None

    data.sort(key=lambda d: d[1])

    return data[0][0]
            


if __name__ == '__main__':  # pragma: no cover
    print("Day with minimum spread is :", min_spread_day())

