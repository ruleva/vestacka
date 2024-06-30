from constraint import *


def constraintML(*variables):
    variable=variables[0]
    s=variable[4:]
    for va in range(1,len(variables)):
        d=variables[va]
        d1=d[4:]
        if s==d1:
            return False
    return True
def constraint(*variables):
    for i in range(len(variables)):
       a,b=variables[i].split("_")
       for j in range(len(variables)):
           c,d=variables[j].split("_")
           #print(a,b,c,d)
           if i!=j and a==c and abs(int(b)-int(d))<=1:
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
    MLDom=[]
    MLDom+= ["ML_vezbi"]
    variablesVk=[]
    variables=[]
    # ---Tuka dodadete gi promenlivite--------------------
    for i in range(int(casovi_AI)):
        variables += [f'AI_cas_{i + 1}']
        variablesVk += [f'AI_cas_{i + 1}']
    problem.addVariables(variables, AI_predavanja_domain)
    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    variables = []
    for i in range(int(casovi_ML)):
        variables += [f'ML_cas_{i + 1}']
        variablesVk += [f'ML_cas_{i + 1}']
        MLDom+=variables
    problem.addVariables(variables, ML_predavanja_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    problem.addConstraint(constraintML, MLDom)
    variables = []
    for i in range(int(casovi_R)):
        variables += [f'R_cas_{i + 1}']
        variablesVk += [f'R_cas_{i + 1}']
    problem.addVariables(variables, R_predavanja_domain)
    variables = []
    for i in range(int(casovi_BI)):
        variables += [f'BI_cas_{i + 1}']
        variablesVk += [f'BI_cas_{i + 1}']
    problem.addVariables(variables, BI_predavanja_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)
    variablesVk += ["AI_vezbi", "ML_vezbi", "BI_vezbi"]
    problem.addConstraint(constraint, variablesVk)
   # problem.addConstraint(AllDifferentConstraint(), variablesVk)
    #print(variablesVk)
    # ---Tuka dodadete gi ogranichuvanjata----------------
    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)
