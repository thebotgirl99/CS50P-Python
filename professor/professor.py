import random

def main():
    level = get_level()
    ques = 10
    tries = 3
    score = 0
    while ques > 0:
        x, y, z = generate_integer(level)
        while tries > 0:
            guess = get_input(x, y)
            if guess != z:
                print("EEE")
                tries -= 1
                continue
            score += 1
            break

        if tries != 3:
            print(f"{x} + {y} = {z}")
            tries =3
        ques -= 1
    print(F"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level:"))
        except ValueError:
            pass
        else:
            if level < 1:
                pass
            elif level > 3:
                pass
            else:
                return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y, (x + y)

    if level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y, (x + y)

    if level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y, (x + y)

def get_input(x, y):
    while True:
        guess = int(input(f"{x} + {y} = "))
        try:
            return guess
        except ValueError:
            return guess


if __name__ == "__main__":
    main()