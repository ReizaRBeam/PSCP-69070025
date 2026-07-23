"""SAESON"""
m = int(input())
k = int(input())
if (m == 12 and k >= 21) or m in (1,2) or (m == 3 and k < 21) :
    print("winter")
elif m in (3,4,5) or (m == 6 and k < 21) :
    print("spring")
elif m in (6,7,8) or (m == 9 and k < 21) :
    print("summer")
elif m in (9,10,11) or (m == 12 and k < 21) :
    print("fall")
