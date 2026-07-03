"""COLORS"""
col1 = input().lower()
col2 = input().lower()
if (col1 not in ("blue","red","yellow")) or (col2 not in ("blue","red","yellow")) :
    print("Error")
elif col1 + col2 in ("redyellow","yellowred") :
    print("Orange")
elif col1 + col2 in ("redblue","bluered") :
    print("Violet")
elif col1 + col2 in ("yellowblue","blueyellow") :
    print("Green")
elif col1 == col2 :
    print("Error")
