def convert(to):
    return to.replace(":)", "🙂").replace(":(", "🙁")

def main():
    user_ip = input("Enter anything ")
    print(convert(user_ip))

main()