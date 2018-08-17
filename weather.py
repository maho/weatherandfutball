from dataparse import min_identifier

def min_spread_day():
    return min_identifier("http://codekata.com/data/04/weather.dat", (0,6), (6,12), (12,18), ignrows=2, ignids=["mo"])
            


if __name__ == '__main__':  # pragma: no cover
    print("Day with minimum spread is :", min_spread_day())

