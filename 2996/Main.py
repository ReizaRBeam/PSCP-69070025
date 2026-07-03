"""word"""
inp = input().lower()
new = ""
for i in range(len(inp)) :
    new += inp[-i - 1]
print(new)
