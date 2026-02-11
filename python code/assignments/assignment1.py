from loguru import logger

labour1 = 'Mahesh'
labour2 = 'Mithilesh'
labour3 = 'Ramesh'
labour4 = 'Sumesh'

# Q1
print("The Labourers are ",labour1,labour2,labour3,labour4)

#Q2

labour1_wage = 500
labour2_wage = 400
labour3_wage = 400
labour4_wage = 300

print(f"Wage of {labour1} is {labour1_wage}, {labour2} is {labour2_wage}, {labour3} is {labour3_wage} and {labour4} is {labour4_wage}")

#Q3

logger.info('\n""" Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that\nwe are implemeting all the logics by ourself. The aim here is to build our \"4 BHK\" house with the\nhelp of \'Python programming\'. We have total land is of \\ 100 ft * 100ft /, to colmplete the house\nwe have total 6 labours with \'different skill set like \"\\\ building wall or building roof \\\\".\n\t\t\tI have to print this paragraph as it is given here.""" ')

#Q7
print(id(labour1),id(labour2),id(labour3),id(labour4))
print(id(labour1_wage),id(labour2_wage),id(labour3_wage),id(labour4_wage))
