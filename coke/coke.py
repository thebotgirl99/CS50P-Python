def main():
    check()

def check():
    t = 50
    while True:
        if t>0:
            cents = int(input("Insert Coin: "))
            if cents == 25 or cents == 10 or cents == 5:
                b = t - cents
                if b < 0:
                    print(f"Change Owed: {cents-t}")
                    break
                print(f"Amount Due: {b}")
                t = b
            else:
                print(f"Amount Due: {t}")
        elif t == 0:
            break

main()

