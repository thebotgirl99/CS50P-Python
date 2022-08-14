def main():
    hours, mins = input("Enter time: ").split(":")
    convert(hours, mins)

def convert(h,m):
    time = round(int(h) + int(m)/60, 2)
    if time >= 7 and time <=8:
        print("breakfast time")
    elif time >=12 and time <=13:
        print("lunch time")
    elif time >=18 and time <=19:
        print("dinner time")

main()