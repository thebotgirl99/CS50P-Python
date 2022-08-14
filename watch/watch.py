import re

def main():
   print(parse(input("HTML: ")))

def parse(s):
    init = re.search("iframe", s, re.IGNORECASE)
    if init:
        if matches := re.search("https?://(?:www\.)?youtube\.com/embed/(\w+)", s, re.IGNORECASE):
            return "https://youtu.be/" + matches[1]
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    main()