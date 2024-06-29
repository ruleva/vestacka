from constraint import *


def constraint1(*vars):
    x = vars[3] + 10 * vars[2] + 100 * vars[1] + 1000 * vars[0]
    y = vars[1] + 10 * vars[-2] + 100 * vars[-3] + 1000 * vars[4]
    res = vars[-1] + 10 * vars[1] + 100 * vars[2] + 1000 * vars[-3] + 10000 * vars[4]
    return x + y == res


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))
        problem.addConstraint(AllDifferentConstraint(), variables)
        problem.addConstraint(constraint1, variables)
    print(problem.getSolution())
