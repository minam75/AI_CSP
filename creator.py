import random

import networkx as nx


def define_n_profs(course_in):
    in_profs = 5

    return in_profs


def create_random(c_list):
    knowledge = list()
    for z in range(len(c_list)):
        knowledge.append(random.randint(20, 100))
    return dict(zip(c_list, knowledge))


def problem_gen(name):
    n_courses = 6
    n_profs = define_n_profs(n_courses)

    out = ''

    out += str(n_courses) + ' ' + str(n_profs) + '\n'

    courses = nx.random_tree(n_courses)

    out += str(len(courses.edges)) + '\n'
    edges = list(courses.edges)
    random.shuffle(edges)
    for item in edges:
        out += str(item[0]) + ' ' + str(item[1]) + '\n'

    profs = list()
    for i in range(n_profs):
        profs.append(create_random(list(courses.nodes)))

    x = 0
    for item in profs:
        y = 0
        for key, value in item.items():
            out += str(value)
            y += 1
            if y < len(item.keys()):
                out += ' '
        x += 1
        if x < len(profs):
            out += '\n'

    file_name = name
    f = open(file_name, 'w')
    f.write(out)
    f.close()


if __name__ == '__main__':
    for i in range(10):
        stri = 'in/input' + str(i + 1) + '.txt'
        problem_gen(stri)
