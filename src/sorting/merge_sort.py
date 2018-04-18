def merge_sort(array):
    if len(array) < 2:
        return array
    else:
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    result = list()
    i = 0
    j = 0
    while True:
        if i >= len(left):
            result += right[j:]
            break
        if j >= len(right):
            result += left[i:]
            break
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    return result


if __name__ == '__main__':
    sample = [int(number) for number in input().split(' ')]
    print(sample)
    sample = merge_sort(sample)
    print(sample)
