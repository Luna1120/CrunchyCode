from loguru import logger 
import math

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistri1 = "Jagmohan"
labour_mistri2 = "Rampyare"
is_home = True

length_of_land = int(input("Enter the length of your land: "))

if (length_of_land < 100):
    logger.info(f"Your length is not sufficient to build a 4 BHK")
    logger.info("Second line")
    if length_of_land > 80:
        logger.info(f"You can build 3 BHK house")
    else:
        logger.info(f"Your land is not having enough space")
elif length_of_land >= 500:
    logger.info(f"You can build more than 2 buildings")
else:
    logger.info(f"Share more details with us")
    logger.info("Third line")


# How will you find out if given number by user is even or odd

number = int(input(f"Enter a number: "))

result = number % 2

if result == 0:
    logger.info(f"{number} is an even number")
else:
    logger.info(f"{number} is an odd number")