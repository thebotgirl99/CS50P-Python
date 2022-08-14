import re

def main():
    ip = input("IPv4 Address: ").strip()
    print(validate(ip))


def validate(ip):
    score = 0
    if matches := re.search(r"(\w+)\.(\w+)\.(\w+)\.(\w+)", ip):
        try:
            for i in range(4):
                if 0 <= int(matches [i+1]) <= 255:
                    score+=1
            if score == 4:
                return True
            else:
                return False
        except ValueError:
            return False
    else:
        return False


if __name__ == "__main__":
    main()