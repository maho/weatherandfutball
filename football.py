from dataparse import min_identifier

def min_for_against():
    return min_identifier("http://codekata.com/data/04/football.dat", 
                          (7,23), (43,47), (50,56), ignrows=1, ignids='-'*17)

