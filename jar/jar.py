class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" *self.size

    def deposit(self, n):
        if n <= (self.capacity-self.size):
            self.size += n
        else:
            raise ValueError("Cookies exceeded my limit")

    def withdraw(self, n):
        if n <= self.size:
            self.size -= n
        else:
            raise ValueError("no more cookies to eat")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 0:
            raise ValueError("Invalid")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if int(size) < 0:
            raise ValueError("Invalid")
        self._size = size

def main():
    cookies = Jar(13)
    cookies.deposit(10)
    cookies.withdraw(9)
    print(cookies)

if __name__ == "__main__":
    main()