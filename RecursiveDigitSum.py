# Author: Birkan Mert Erenler
# https://www.hackerrank.com/challenges/recursive-digit-sum/problem

def superDigitInteger(p):
    n = str(p)
    if len(n) == 1:
        return p
    else:
        midpoint = int(len(n)/2)
        return superDigitInteger(superDigitInteger(int(n[:midpoint])) 
                                    + superDigitInteger(int(n[midpoint:])))

def superDigit(n, k):
    if len(n) == 0:
        return 0
    elif len(n) == 1:
        return superDigitInteger(int(n)*k)
    else:
        midpoint = int(len(n)/2)
        return superDigitInteger(superDigit(n[:midpoint], k) 
                                    + superDigit(n[midpoint:], k))