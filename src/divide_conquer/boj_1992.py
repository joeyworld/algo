def compress(image):
    dimension = len(image)
    # base case
    if image == [['1'] * dimension] * dimension:
        return '1'
    elif image == [['0'] * dimension] * dimension:
        return '0'
    else:
        # recursive call
        mid = dimension // 2
        # divide
        left_up = compress([row[:mid] for row in image[:mid]])
        right_up = compress([row[mid:] for row in image[:mid]])
        left_down = compress([row[:mid] for row in image[mid:]])
        right_down = compress([row[mid:] for row in image[mid:]])
        # conquer
        return '({}{}{}{})'.format(left_up, right_up, left_down, right_down)


if __name__ == '__main__':
    N = int(input())
    image = [list(input()) for _ in range(N)]
    print(compress(image))
