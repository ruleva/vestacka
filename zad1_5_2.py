from constraint import *
def ML_constraint(*v):
    for i in range(len(v)):
        for j in range(len(v)):
            if i!=j:
                t1=v[i]
                t1=t1[-1:]
                t2=v[j]
                t2=t2[-1:]
                if t1==t2:
                    return False
    return True
def twoHourConstraint(*v):
    for i in range(len(v)):
        for j in range(len(v)):
            if i != j:
                t1 = v[i]
                day1 = t1[:3]
                t2 = v[j]
                day2 = t2[:3]
                time1=t1[-1:]
                time2=t2[-1:]
                if day1 == day2:
                    if abs(int(time1) - int(time2))<2:
                        return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]
    allVariables=[]
    allVariables+=['AI_vezbi','ML_vezbi','BI_vezbi']
    problem.addVariables(['AI_vezbi'],AI_vezbi_domain)
    problem.addVariables(['ML_vezbi'], ML_vezbi_domain)
    problem.addVariables(['BI_vezbi'], BI_vezbi_domain)
    variables=[]
    for i in range(int(casovi_AI)):
        variables+=[f'AI_cas_{i+1}']
    allVariables+=variables
    problem.addVariables(variables,AI_predavanja_domain)
    variables=[]
    for i in range(int(casovi_ML)):
        variables+=[f'ML_cas_{i+1}']
    allVariables += variables
    problem.addVariables(variables, ML_predavanja_domain)
    problem.addConstraint(ML_constraint,variables+['ML_vezbi'])
    variables = []
    for i in range(int(casovi_R)):
        variables+=[f'R_cas_{i+1}']
    allVariables += variables
    problem.addVariables(variables, R_predavanja_domain)
    variables = []
    for i in range(int(casovi_BI)):
        variables += [f'BI_cas_{i+1}']
    allVariables += variables
    problem.addVariables(variables, BI_predavanja_domain)
    variables = []
    # ---Tuka dodadete gi promenlivite--------------------
    problem.addConstraint(AllDifferentConstraint(),allVariables)
    problem.addConstraint(twoHourConstraint,allVariables)
    # ---Tuka dodadete gi ogranichuvanjata----------------
    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)
