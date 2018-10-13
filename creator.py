from random import randint

import networkx as nx


def define_n_profs(course_in):
    in_profs = randint(course_in // 2, course_in)

    return in_profs


def create_random(c_list):
    knowledge = list()
    for z in range(len(c_list)):
        knowledge.append(randint(20, 100))
    return dict(zip(c_list, knowledge))


if __name__ == '__main__':
    n_courses = randint(10, 30)
    n_profs = define_n_profs(n_courses)

    out = ''

    out += str(n_courses) + ' ' + str(n_profs) + '\n'

    courses = nx.random_tree(n_courses)

    out += str(len(courses.edges)) + '\n'
    for item in courses.edges:
        out += str(item[0]) + ' ' + str(item[1]) + '\n'

    profs = list()
    for i in range(n_profs):
        profs.append(create_random(list(courses.nodes)))

    out += '\n'
    for item in profs:
        for key, value in item.items():
            out += str(key) + ' ' + str(value) + '\n'

    file_name = 'inputs/input.txt'
    f = open(file_name, 'w')
    f.write(out)
    f.close()