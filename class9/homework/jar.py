class Jar:
    def __init__(self, capacity=12):
        if int(capacity)<0:
            raise ValueError
        self._capacity = capacity
        self._size =0


    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        if n +self.size > self.capacity:
            raise ValueError
        self._size = self.size+n
        return self.size

    def withdraw(self, n):
        if n >self.size:
            raise ValueError
        self._size = self.size-n
        return self.size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
