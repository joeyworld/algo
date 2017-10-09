def qsort(arr):
    n = len(arr)
    if n < 2:
        return arr
    else:
        p_index = n - 1
        pivot = arr[p_index]
        # partition
        i = 0
        while True:
            if i >= p_index:
                break
            elif arr[i] >= pivot:
                arr.append(arr[i])
                del arr[i]
                p_index -= 1
            else:
                i += 1
        # recursive call
        return qsort(arr[:p_index]) + [pivot] + qsort(arr[p_index + 1:])


if __name__ == '__main__':
    sample = [int(number) for number in input().split(' ')]
    print(sample)
    sample = qsort(sample)
    print(sample)
