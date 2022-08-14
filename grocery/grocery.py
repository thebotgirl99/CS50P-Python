dict = {}
while True:
    try:
        item = input().strip().upper()
    except EOFError:
        for x in sorted(dict):
            print(str(dict[x]) + " " + x)
        break
    else:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
