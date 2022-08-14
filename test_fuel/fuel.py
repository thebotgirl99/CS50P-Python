def main():
    while True:
        try:
            ip = input("Fraction: ").strip()
            convert(ip)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            per = convert(ip)
            print(gauge(per))
            break

def convert(ip):
        try:
            x , y = ip.split("/")
            x = int(x)
            y = int(y)
            if x > y and y!=0:
                raise ValueError()
            per = round((x/y)*100)
        except (ValueError):
            raise ValueError()
        except (ZeroDivisionError):
            raise ZeroDivisionError()
        else:
            return per

def gauge(per):
    if per<=1:
        return("E")
    elif per>=99:
        return("F")
    else:
        return(f"{per}%")

if __name__ == "__main__":
    main()

