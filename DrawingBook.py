# Author: Birkan Mert Erenler
# https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n, p):
    dist_begin = p
    dist_end = n - p

    count_begin = math.floor(dist_begin / 2)
    if n % 2 == 0:
        count_end = math.ceil(dist_end / 2)
    else:
        count_end = math.floor(dist_end / 2)
    
    return min([count_end, count_begin])