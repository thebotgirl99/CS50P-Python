import sys
import csv

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) >3:
    sys.exit("Too many command-line arguments ")
else:
    ext = sys.argv[1].split(".")
    if ext[1] != "csv":
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1], "r") as r_file:
                reader = csv.DictReader(r_file, delimiter=",")
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
        else:
            with open(sys.argv[1], "r") as r_file:
                reader = csv.DictReader(r_file)

                with open(sys.argv[2], "w") as w_file:
                    writer = csv.DictWriter(w_file, fieldnames=["first", "last", "house"])

                    writer.writeheader()

                    for row in reader:
                        last, first = row["name"].split(",")
                        house = row["house"]

                        writer.writerow({"first": first.strip(), "last": last, "house": house})


