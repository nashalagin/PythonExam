class MySimpleIter:
    def __init__(self, N):
        self.start, self.end = 2, N

    def __iter__(self):
        return self

    def __next__(self):
        n = MySimpleIter.__searchSimpleNumber(self.start)
        if n < self.end:
            self.start = n + 1
            return n
        else:
            raise StopIteration

    def __searchSimpleNumber(n):
        for i in range(2, n):
            if n % i == 0:
                return MySimpleIter.__searchSimpleNumber(n+1)
        return n

if __name__ == "__main__":
    for i in MySimpleIter(100):
        print(i, end=" ")