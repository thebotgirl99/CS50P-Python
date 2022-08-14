def main():
    x, y, z = input("Enter x, y and z: ").strip().split(" ")
    print(round(float(math(x,y,z)),1))

def math(x,y,z):
    if y == "*":
        return int(x)*int(z)
    elif y == "+":
        return int(x)+int(z)
    elif y == "-":
        return int(x)-int(z)
    else:
        return int(x)/int(z)

main()