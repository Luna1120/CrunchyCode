from loguru import logger 
import math

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistri1 = "Jagmohan"
labour_mistri2 = "Rampyare"
is_home = True

# Calculate the total area of land

total_area_of_land = length_of_land * breadth_of_land

perimeter_of_land = 2 * (length_of_land + breadth_of_land)

logger.info(f"Total area of my land is {total_area_of_land} ")
logger.info(f"Perimeter of land is {perimeter_of_land}")

# print(15/7)
# print(15//7)

# print(math.ceil(15//7))

# a="25"
# b=25
# print(a+str(b))

length_of_land = float(input("Please enter length of your land: "))
breadth_of_land = input("Please enter breadth of your land: ")
# logger.info(f"{type(length_of_land)}")
total_area_of_land = abs(length_of_land*float(breadth_of_land))
logger.info(f"Total area of your land is {total_area_of_land} sq.ft")