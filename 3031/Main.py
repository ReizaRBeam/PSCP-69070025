"""INKU"""
import math as m
inp = input().split(" ")
for i in range(int(inp[1])) :
    loc = input().split(" ")
    ran = m.sqrt(int(loc[0])** 2 + int(loc[1])** 2)
    dis = (ran ** 2) * 3.1416
    dis /= int(inp[0])
    if dis and dis != int(dis) :
        print(int(dis) + 1)
    elif dis == int(dis) :
        print(int(dis))
    else :
        i = 0
        print(i)
