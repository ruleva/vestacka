from constraint import *


def constraint(*papers):
    #print(papers)
    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0
    for paper in papers:
        if paper == 'T1':
            t1 += 1
        elif paper == 'T2':
            t2 += 1
        elif paper == 'T3':
            t3 += 1
        else:
            t4 += 1
    if t1 > 4 or t2 > 4 or t3 > 4 or t4 > 4:
        return False
    return True


def sameConstraint(*lista1):
    # p1 = lista1[0]
    # for paper in lista1:
    #     if p1 != paper:
    #         return False
    # return True
    return len(set(lista1)) == 1


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()
    # Tuka definirajte gi promenlivite
    ...
    variables = [f'{title} ({papers[title]})' for title in papers]
    domain = [f'T{i + 1}' for i in range(num)]
    # print(variables)
    # print(domain)
    problem = Problem(BacktrackingSolver())
    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)
    problem.addConstraint(constraint, tuple(variables))
    # Tuka dodadete gi ogranichuvanjata
    ...
    predmeti = tuple(papers.values())
    for p in predmeti:
        lista = []
        for v in variables:
            if p in v:
                lista.append(v)
        if len(lista)<=4:
            problem.addConstraint(sameConstraint, lista)

    result = problem.getSolution()
    if result is not None:
        for i in variables:
                print(f'{i}: {result[i]}')

    # Tuka dodadete go kodot za pechatenje
    ...
