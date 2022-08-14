list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def num():
    while True:
        date = input("Date: ").strip().title()
        if "/" in date:
            month, day, year = date.split("/",2)
            month = int(month)
            day = int(day)
            year = int(year)
            if month <= 12 and day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break
        elif "," in date:
            month, day, year = date.split(" ",2)
            day = int(day.strip(","))
            year = int(year)
            if month in list and day <= 31:
                print(f"{year}-{list.index(month)+1:02}-{day:02}")
                break
        else:
            pass
num()
