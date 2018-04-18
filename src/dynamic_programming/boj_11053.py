def find_ideal_pos(sorted_list, begin, end, element):
    mid = (begin + end) // 2
    if element <= sorted_list[begin]:
        return begin
    if element >= sorted_list[end]:
        return end
    if end - begin == 1:
        return end

    if sorted_list[mid - 1] < element <= sorted_list[mid]:
        return mid
    elif sorted_list[mid] < element:
        return find_ideal_pos(sorted_list, mid, end, element)
    else:
        return find_ideal_pos(sorted_list, begin, mid, element)


def find_lis(given, length):
    lis = [given[0]]
    top = given[0]
    lis_length = 1

    for i in range(1, length):
        if top < given[i]:
            top = given[i]
            lis.append(given[i])
            lis_length += 1
        else:
            ideal_pos = find_ideal_pos(lis, 0, lis_length - 1, given[i])
            lis[ideal_pos] = given[i]
            top = lis[lis_length - 1]

    return lis_length


def main():
    N = int(input())
    input_sequence = input().split(' ')
    input_sequence = [int(element) for element in input_sequence]

    print(find_lis(input_sequence, N))


if __name__ == '__main__':
    main()
