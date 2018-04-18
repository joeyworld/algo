def selection(numbers, k):
    """
    finds kth smallest number within numbers
    :param numbers: number list
    :param k: natural number. Order of smallest number
    :return: kth smallest number of list
    """

    # select the pivot
    n = len(numbers)
    p_index = n - 1
    pivot = numbers[p_index]

    # arrange number as quick sort-wise
    i = 0
    while True:
        if i >= p_index:
            break
        elif numbers[i] >= pivot:
            numbers.append(numbers[i])
            del numbers[i]
            p_index -= 1
        else:
            i += 1

    if numbers[k - 1] == pivot:
        return pivot
    elif numbers[k - 1] < pivot:
        return selection(numbers[:p_index], k)
    else:
        return selection(numbers[p_index + 1:], k - (p_index + 1))


if __name__ == '__main__':
    sample = [int(number) for number in input().split(' ')]
    print(sample)
    print('Enter k :', end=' ')
    print(selection(sample, int(input())))
