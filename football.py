from dataparse import min_identifier

def min_for_against():
    return min_identifier("http://codekata.com/data/04/football.dat", 
                          (7,23), (43,47), (50,56), ignrows=1, ignids='-'*17)


if __name__ == '__main__':  # pragma: no cover
    print('Team with min for-against difference is  :', min_for_against())



