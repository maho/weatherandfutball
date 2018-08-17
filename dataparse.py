from urllib.request import urlopen

def val(b):
    return float(b.strip().replace(b"*", b""))


def min_identifier(url, idrange, hirange, lorange, ignrows=2, ignids=None):
    """
        parse fixed size column data file under url, 
        for each row calculate difference between hi and lo column and return 
        id of row which has the smallest difference

        url - url of data file
        idrange - range of id column in row (eg. (1, 10))
        hirange - range of column - hi val
        lorange - range of column - lo val
        ignrows - how many rows to ignore?
        ignids - which identifiers should be ignored
    """
    
    data = []
    with urlopen(url) as request:
        # ignore rows and empty line
        for __ in range(ignrows):
            request.readline()

        for line in request:
            if not line or line.startswith(b"---"):
                continue
            idrow = line[slice(*idrange)].strip().decode()
            if ignids and idrow in ignids:
                break  # last line, ignored

            maxt = val(line[slice(*hirange)])
            mint = val(line[slice(*lorange)])

            data.append((idrow, maxt - mint))

    if not data:
        return None

    data.sort(key=lambda d: d[1])

    return data[0][0]

