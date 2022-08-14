import re

def main():
    ans = convert(input("Hours: ").strip())
    print(ans)

def convert(s):
    matches = re.search(r"(\d+):?(\d+)? (AM|PM) to (\d+):?(\d+)? (PM|AM)", s, re.IGNORECASE)
    if matches:
        if matches[2] or matches[5]:
            if int(matches[2]) < 60 and int(matches[5]) < 60:
                if matches[3] == "AM" and matches[6] == "PM":
                    a = int(matches[1])
                    ad = int(matches[2])
                    p = int(matches[4]) + 12
                    pd = int(matches[5])
                    if a == 12:
                        a = 0
                    if p == 24:
                        p = 12
                    ans = f"{a:02}:{ad:02} to {p:02}:{pd:02}"
                else:
                    a = int(matches[1])+12
                    ad = int(matches[2])
                    p = int(matches[4])
                    pd = int(matches[5])
                    if p == 12:
                        p = 0
                    if a == 24:
                        a = 12
                    ans = f"{a:02}:{ad:02} to {p:02}:{pd:02}"
                return(ans)
            else:
                raise ValueError()
        else:
            if matches[3] == "AM" and matches[6] == "PM":
                a = int(matches[1])
                ad = 0
                p = int(matches[4])+12
                pd = 0
                if a == 12:
                    a = 0
                if p == 24:
                    p = 12
                ans = f"{a:02}:{ad:02} to {p:02}:{pd:02}"
                return(ans)
            else:
                a = int(matches[1])+12
                ad = 0
                p = int(matches[4])
                pd = 0
                if p == 12:
                    p = 0
                if a == 24:
                    a = 12
                ans = f"{a:02}:{ad:02} to {p:02}:{pd:02}"
                return(ans)
    else:
        raise ValueError()


if __name__ == "__main__":
    main()