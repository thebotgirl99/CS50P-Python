from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    ans  = get_mins(input("Date of Birth: "))
    print(ans)

def get_mins(bday):
    matches = re.search(r"^(\d+)-(\d+)-(\d+)$", bday)
    if not matches:
        sys.exit("Invalid date")
    elif int(matches[2]) > 12 or int(matches[3]) > 31:
        print(int(matches[2]))
        sys.exit("Invalid date")
    else:
        today = date.today()
        my_bday = date(int(matches[1]), int(matches[2]), int(matches[3]))
        num_days = abs(my_bday - today)
        num_mins = num_days.days * 24 * 60
        words = p.number_to_words(num_mins, andword="")
        return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()