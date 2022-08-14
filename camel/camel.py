def main():
    camelCase = input("camelCase: ")
    print("snake_case: ", end="")
    snake_case(camelCase)

def snake_case(s):
    for c in s:
        if c.islower():
            print(c, end="")
        else:
            print(f"_{c.lower()}", end="")
    print()

main()