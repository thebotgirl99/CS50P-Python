def main():
    while True:
        try:
            x , y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
        except (ValueError):
            pass
        else:
            if x>y or y == 0:
                pass
            else:
                gauge(x,y)
                break

def gauge(x,y):
    per = round((x/y)*100)
    if per<=1:
        print("E")
    elif per>=99:
        print("F")
    else:
        print(f"{per}%")

main()

