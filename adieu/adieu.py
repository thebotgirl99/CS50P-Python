import inflect
list = []
p = inflect.engine()

while True:
    try:
        ip = input("Name: ")
    except EOFError:
        print()
        new = p.join((list))
        print(f"Adieu, adieu, to {new}")
        break
    else:
        list.append(ip)
        print(list)
        pass

