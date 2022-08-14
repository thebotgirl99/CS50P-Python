def main():
    user_ip = input("Input: ").strip()
    print("Output: ", end="")
    print(shorten(user_ip))

def shorten(u):
    v = ["a", "e", "i", "o", "u"]
    for c in u:
        for i in range(len(v)):
            if c.lower() == v[i]:
                u = u.replace(c,"")
    return(u)

if __name__ == "__main__":
    main()


