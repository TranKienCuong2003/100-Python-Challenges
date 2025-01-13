class DivisibleBy7:
    def __init__(self, n):
        self.n = n

    def generate(self):
        for i in range(0, self.n + 1):
            if i % 7 == 0:
                yield i

n = int(input("Enter the value of n: "))
div_by_7 = DivisibleBy7(n)

for number in div_by_7.generate():
    print(number)
