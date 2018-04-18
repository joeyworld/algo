def solve(students_info, num_students):
    # sort by korean score
    students_info = sorted(
        students_info, key=lambda x: x['korean'], reverse=True)
    for student in students_info:
        print(student)
    # sort by english score within same korean scores
    students_info = sort_within_conditions(
        students_info, num_students, key='english')
    print()
    for student in students_info:
        print(student)
    # sort by math score within same korean & english scores
    students_info = sort_within_conditions(
        students_info, num_students, key='math', reverse=True)
    print()
    for student in students_info:
        print(student)
    # sort by alphabetical order within same scores of all subjects
    students_info = sort_within_conditions(
        students_info, num_students, key='name')
    print()
    for student in students_info:
        print(student)

    return students_info


def sort_within_conditions(students_info, num_students, key, **kwargs):
    # sort_within_conditions(students, 4, key='math')
    # sort_within_conditions(students, 10, key='name')
    start_index, end_index = 0, 1
    while end_index < num_students:
        # test
        print(students_info[start_index].keys())
        print(students_info[start_index].values())

        student1_scores = set(students_info[start_index].values()[
                              0:students_info[start_index].keys().index(key)])
        student2_scores = set(students_info[end_index].values()[
                              0:students_info[end_index].keys().index(key)])
        if len(student1_scores ^ student2_scores) == 0:
            students_info[start_index:end_index] = sorted(
                students_info[start_index:end_index], key=lambda x: x[key], **kwargs)
            start_index = end_index
        end_index += 1

    return students_info


if __name__ == '__main__':
    num_students = int(input())
    students_info = list()
    for i in range(num_students):
        name, korean, english, math = input().split(' ')
        single_student = {
            'korean': int(korean),
            'english': int(english),
            'math': int(math),
            'name': name
        }
        students_info.append(single_student)

    students_info = solve(students_info, num_students)
    # for student in students_info:
    #     print(student['name'])
