"""VOTE"""
suma = float(input())
high = float(input())
low = 0
if high * 2 <= suma :
    low = suma - (high * 2)
if high - low > 2 :
    print("Surprising")
else :
    print("Not surprising")
