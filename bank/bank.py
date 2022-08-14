user_ip = input("Enter your greetings: ").lstrip().casefold()

if user_ip.find("hello") == 0:
    print("$0")
elif user_ip.find("h") == 0:
    print("$20")
else:
    print("$100")


