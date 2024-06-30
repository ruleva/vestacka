from constraint import *
def constraint(*v):
    t1=0
    t2=0
    t3=0
    t4=0

    for i in range(len(v)):
        if v[i] == 'T1':
            t1+=1
        elif v[i] == 'T2':
            t2+=1
        elif v[i] == 'T3':
            t3+=1
        else:
            t4+=1
    if t1 > 4 or t2 > 4 or t3 > 4 or t4 >4:
        return False
    return True
def num_constraint(*v):
    if len(v)<=4:
        c=v[0]
        for i in range(1,len(v)):
            if c!=v[i]:
                return False
    return True
if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables=[f'{title} ({papers[title]})' for title in papers]
    ai=[]
    ml=[]
    nlp=[]
    for title1 in papers:
        if papers[title1] == "AI":
            ai.append(f'{title1} ({papers[title1]})')
        elif papers[title1] == "ML":
            ml.append(f'{title1} ({papers[title1]})')
        elif papers[title1] == "NLP":
            nlp.append(f'{title1} ({papers[title1]})')
    # print(ai)
    # print(ml)
    # print(nlp)
    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)
    problem.addConstraint(num_constraint,ai)
    problem.addConstraint(num_constraint, ml)
    problem.addConstraint(num_constraint, nlp)

    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(constraint,variables)

    result = problem.getSolution()
    for v in result:
        if v.split(" ")[0] == 'Paper10':
            s=f'{v}: {result[v]}'
        else:
            print(f'{v}: {result[v]}')
    print(s)

    # Tuka dodadete go kodot za pechatenje
    ...
