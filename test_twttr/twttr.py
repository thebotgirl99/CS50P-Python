def main():
    user_ip = input("Input: ").strip()
    print("Output: ", end="")
    print(shorten(user_ip))

def shorten(u):
    v = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for c in u:
        for i in range(len(v)):
            if c == v[i]:
                u = u.replace(c,"")
    return(u)

if __name__ == "__main__":
    main()


