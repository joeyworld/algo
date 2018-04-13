final_answer = [0 for _ in range(10)]


def solve(N, digit):
    numbers_by_bound = sorted(list(set(split_number(N, digit))))
    print(numbers_by_bound)
    n = len(numbers_by_bound)
    for i in range(n - 1):
        find_digit(numbers_by_bound[i], numbers_by_bound[i + 1] - 1)


def find_digit(start, end):
    digit = len(str(start))
    print()
    print('전체 {}부터 {}까지, {}자리 수'.format(start, end, digit))

    for i in range(1, digit + 1):
        divisor = 10 ** i
        start_endpoint = start % divisor
        end_endpoint = end % divisor

        print('{}의 자리 : {} 에서 {} 까지'.format(divisor // 10, start_endpoint, end_endpoint))


def split_number(limit, digit):
    numbers = list()
    for i in range(digit):
        numbers.append(10 ** i)

    temp = list()

    for i in range(digit):
        temp.append((limit // 10 ** i) * (10 ** i))

    temp = reversed(temp)
    numbers += temp

    numbers[-1] += 1
    return numbers


if __name__ == '__main__':
    N = input()
    digit = len(N)
    solve(int(N), digit)
    [print(num, end=' ') for num in final_answer]
    print()
