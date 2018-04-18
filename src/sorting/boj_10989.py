def radix_sort(numbers):
    max_number = max(numbers)
    sorted_numbers = list()
    i = 1

    while True:
        n = len(numbers)
        digit_numbers = [
            number for number in numbers if 0 < number // i < 10]

        digit_numbers.sort()
        sorted_numbers += digit_numbers
        i *= 10

        if max_number in digit_numbers:
            break

    return sorted_numbers


if __name__ == '__main__':
    N = int(input())
    numbers = radix_sort([int(input()) for _ in range(N)])
    for number in numbers:
        print(number)
