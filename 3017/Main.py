"""GIMME YO MONEY"""
pay = int(input())
rec = pay / 10
if rec > 1000 :
    rec = 1000
elif rec < 50 :
    rec = 50
pay += rec

pay *= 1.07
print(f"{pay:.2f}")
