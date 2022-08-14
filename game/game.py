from random import randint

def main():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        else:
            if n <= 0:
                pass
            else:
                check(n)
                break

def check(n):
    r = randint(1,n)
    while True:
        try:
            g = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if g <= 0:
                pass
            elif g < r:
                print("Too small!")
                break
            elif g > r:
                print("Too large!")
                break
            else:
                print("Just right!")
                break
main()


