# Fractional Knapsack Problem
# Splitting product is allowed


def solve_fractional_knapsack(goods_list, max_weight):
    goods_list = sorted(
        goods_list, key=lambda x: x['price'] / x['weight'], reverse=True)

    knapsack = list()
    i = 0
    available_weight = max_weight
    while True:
        knapsack.append(goods_list[i])
        available_weight -= goods_list[i]['weight']
        if available_weight == 0:
            break
        elif available_weight < 0:
            knapsack[i]['weight'] += available_weight
            break
        i += 1
    print_solution(knapsack)


def print_solution(knapsack):
    for good in knapsack:
        print('{} gram(s) of {}'.format(good['weight'], good['name']))


if __name__ == '__main__':
    # sample goods, price, and weight
    sample_goods = [
        {
            'name': 'platinum',
            'weight': 10,
            'price': 600000,
        },
        {
            'name': 'tin',
            'weight': 50,
            'price': 50000,
        },
        {
            'name': 'silver',
            'weight': 25,
            'price': 100000,
        },
        {
            'name': 'gold',
            'weight': 15,
            'price': 750000,
        },
    ]
    solve_fractional_knapsack(sample_goods, 40)
