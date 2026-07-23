"""CIRCLE"""
tem = float(input())
fir = input().upper()
sec = input().upper()

if fir == "C" :
    if sec == "K" :
        tem += 273.15
    elif sec == "F" :
        tem = (tem * 1.8) + 32
    elif sec == "R" :
        tem = (tem + 273.15) * 1.8
elif fir == "K" :
    if sec == "C" :
        tem -= 273.15
    elif sec == "F" :
        tem = (tem - 273.15) * 1.8 + 32
    elif sec == "R" :
        tem *= 1.8
elif fir == "F" :
    if sec == "K" :
        tem = ((tem - 32) / 1.8) + 273.15
    elif sec == "C" :
        tem = (tem - 32) / 1.8
    elif sec == "R" :
        tem += 459.67
elif fir == "R" :
    if sec == "K" :
        tem /= 1.8
    elif sec == "C" :
        tem = (tem / 1.8) - 273.15
    elif sec == "F" :
        tem -= 459.67
print(f"{tem:.2f}")
