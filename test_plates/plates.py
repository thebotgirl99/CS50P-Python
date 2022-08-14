import sys

def main():
    user_input = input("Enter Name: ")
    if is_valid(user_input):
        print("valid")
        sys.exit(0)
    else:
        print("invalid")
        sys.exit(1)


def is_valid(input_string):
    if len(input_string) > 6 or len(input_string) < 2:
        return False

    if not input_string[0].isalpha() and not input_string[1].isalpha():
        return False
    counter = 0
    while counter < len(input_string):
        if input_string[counter].isdigit():
            if input_string[counter] == '0':
                return False
            else:
                break
        counter = counter + 1

    for each in input_string:
        if each in ['.' ,'!' ,'?' ,' ', ',']:
            return False

    for i,c in enumerate(input_string):
        if c.isdigit():
            temp = input_string[i:]
            if is_number(temp) != True:
                return False
            else:
                break
    return True

def is_number(s):
    for each in s:
        if each.isdigit() == False:
            return False
    return True

if __name__ == "__main__":
    main()