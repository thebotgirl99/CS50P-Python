import sys
num_lines = 0
row = []

if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) >2:
    sys.exit("Too many command-line arguments ")
else:
    ext = sys.argv[1].split(".")
    if ext[1] != "py":
        sys.exit("Not a Python file")
    else:
        try:
            file = open(sys.argv[1], "r")
            lines = file.readlines()
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            for line in lines:
                if line.strip().startswith("#") or line.isspace() == True:
                    pass
                else:
                    num_lines += 1
            print(num_lines)




