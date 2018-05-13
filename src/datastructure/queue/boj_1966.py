printer_queue = {
    'front': 0,
    'back': 0
}
all_documents = dict()


def solve(N, M, docs):
    # TODO enqueue all docs
    for i in range(N):
        printer_queue[i] = docs[i]
        printer_queue['back'] += 1
        if docs[i] not in all_documents:
            all_documents[docs[i]] = 1
        else:
            all_documents[docs[i]] += 1

    print(printer_queue)
    print(all_documents)
    # TODO find M in queue
    # TODO find its priority


def main():
    N, M = input().split(' ')
    docs = input().split(' ')

    N = int(N)
    M = int(M)
    docs = [int(element) for element in docs]

    print(solve(N, M, docs))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
