def quick_sort(num_list):
    n = len(num_list)
    if n < 2:
        return num_list
    else:
        mid = n // 2
        pivot = num_list[mid]
        pivot_left = list()
        pivot_right = list()
        for num in num_list:
            if num < pivot:
                pivot_left.append(num)
            elif num > pivot:
                pivot_right.append(num)
        return quick_sort(pivot_left) + [pivot] + quick_sort(pivot_right)


def test_qsort(mid, pivot, current, left, right):
    print('=' * 50)
    print('mid = {}'.format(mid))
    print('current pivot = {}'.format(pivot))
    print('original list = {}'.format(current))
    print('left of pivot = {}'.format(left))
    print('right of pivot = {}'.format(right))
    print('=' * 50)


if __name__ == '__main__':
    sample = [2, 4, 10, 7, 1, 6, 9, 3, 8, 5]
    print(sample)
    sample = quick_sort(sample)
    print(sample)
