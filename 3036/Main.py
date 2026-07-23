"""FORT"""
loc = int(input())
new = loc
a = 0
row = 0
mod = loc % 2
for i in range(loc) :
    new -= ((i * 2) + 1)
    row += 1
    if new <= 0 :
        a = i * 2
        if row % 2 != mod :
            a -= 1
        break

print(a)
