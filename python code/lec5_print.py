# print("Programming aasaan hai")
# variable

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistri1 = "Jagmohan"
labour_mistri2 = "Rampyare"
is_home = True

# print("length of land is",length_of_land)
# print('Labour name is',labour_mistri1)
# print("My home is of 4 bhk \nLength of the total land is 100")

# print("""My home is of 4 bhk 
# Length of the total land is 100""")

# print("My home is of \t \"4 bhk\" ")

# print(length_of_land,bricks_cost_per_piece,labour_mistri1,is_home)

# print(type(length_of_land),type(bricks_cost_per_piece),type(labour_mistri1),type(is_home))

# f string and .format method

print(f"cost of bricks per unit is {bricks_cost_per_piece} {length_of_land} {labour_mistri2}")
print("cost of bricks per unit is {} {} {}".format(bricks_cost_per_piece,length_of_land,labour_mistri2))

from loguru import logger

logger.info(f"cost of bricks per unit is {bricks_cost_per_piece}")