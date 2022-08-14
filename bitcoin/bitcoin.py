import sys
import requests

def main():
    number = get_n()
    rate = price()
    print(f"${number*rate:,.4f}")

def get_n():
    try:
        num = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        return num

def price():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    obj = response.json()
    rate = obj["bpi"]["USD"]["rate_float"]
    return rate

main()



