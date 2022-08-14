def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    n = len(s)
    if 2 <= n <= 6 and s.isalnum()==True and s[0:2].isalpha()==True:
        last = s[2:n+1]
        if last.isalnum()==True and last[len(last)-1].isalpha()==False:
            for c in last:
                if c.isnumeric()==True:
                    if c == "0":
                        return False
                    else:
                        for i in range(len(last)):
                            if last[i].isnumeric==True and last[i+1:len(last)-1].isalnum==True:
                                return False
                return True
        elif last.isalpha()==True:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()