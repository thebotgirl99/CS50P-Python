def main():
    user_ip = input("Enter your greetings: ").lstrip()
    ans = value(user_ip)
    print(f"${ans}")

def value(user_ip):
    if user_ip.lower().find("hello") == 0:
        return 0
    elif user_ip.lower().find("h") == 0:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
