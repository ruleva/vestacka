from constraint import *


def constraint(simona, marija, petar, meeting):
    simona_slobodni = (13, 14, 16, 19)
    petar_slobodni = (12, 13, 16, 17, 18, 19)
    marija_slobodni = (14, 15, 18)
    sim = 0
    pet = 0
    mar = 0
    if simona == 0 or meeting not in simona_slobodni:
        return False
    else:
        if meeting in simona_slobodni and simona == 1:
            sim = 1
        if meeting in petar_slobodni and meeting in simona_slobodni and petar == 1:
            pet = 1
        if meeting in marija_slobodni and meeting in simona_slobodni and marija == 1:
            mar = 1
    if sim == 1 and (mar + pet == 1) and (marija + petar == 1):
        return True
    else:
        return False


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [12, 13, 14, 15, 16, 17, 18, 19])

    # ----------------------------------------------------
    problem.addConstraint(constraint, ("Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"))
    # ---Tuka dodadete gi ogranichuvanjata----------------

    # ----------------------------------------------------
    solutions = problem.getSolutions()
    for solution in solutions:
        print({'Simona_prisustvo': solution['Simona_prisustvo'],
               'Marija_prisustvo': solution['Marija_prisustvo'],
               'Petar_prisustvo': solution['Petar_prisustvo'],
               'vreme_sostanok': solution['vreme_sostanok']})
