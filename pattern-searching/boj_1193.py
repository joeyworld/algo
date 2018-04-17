def find_numerator_denominator(num):
    denominator = -1
    numerator = -1

    index = 1
    total = 0
    previous_total = 0
    while True:
        previous_total = total
        total += index
        if total >= num:
            break
        index += 1

    if index % 2 == 0:
        denominator = num - previous_total
        numerator = (index + 1) - denominator
    else:
        numerator = num - previous_total
        denominator = (index + 1) - numerator

    return (denominator, numerator)


def main():
    X = int(input())
    fraction = find_numerator_denominator(X)
    print('{}/{}'.format(fraction[0], fraction[1]))


if __name__ == '__main__':
    main()
