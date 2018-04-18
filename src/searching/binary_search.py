A = [i for i in range(1, 11)]
print(A)


def binary_search(k):
    left = 0
    right = len(A) - 1
    while True:
        mid = (right + left) // 2
        if A[mid] == k:
            return A[mid]
        elif A[mid] < k:
            # print('target = {}, found = {}'.format(k, A[mid]))
            left = mid + 1
        else:
            # print('target = {}, found = {}'.format(k, A[mid]))
            right = mid - 1
    else:
        return None


print(binary_search(11))
print(binary_search(8))
