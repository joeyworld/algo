def solve(people_info):
    people_info = sorted(people_info, key=lambda x: x['age'])
    return people_info


if __name__ == '__main__':
    num_people = int(input())
    people_info = list()

    for i in range(num_people):
        age, name = input().split(' ')
        single_people = {
            'key': i,
            'age': int(age),
            'name': name
        }
        people_info.append(single_people)

    people_info = solve(people_info)
    for person in people_info:
        print('{} {}'.format(person['age'], person['name']))
