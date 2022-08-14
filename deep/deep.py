user_ip = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip().casefold()

if user_ip == "42" or user_ip == "forty-two" or user_ip == "forty two":
    print("Yes")
else:
    print("No")