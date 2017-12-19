n = int(input())
digits = list()

while n > 0:
    digits.append(n % 10)
    n //= 10

digits.sort(reverse=True)

for digit in digits:
    print(digit, end='')
