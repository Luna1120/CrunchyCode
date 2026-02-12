from loguru import logger

# Assignment
# Print all the even numbers from 1 to 100

for number in range(101):
    if number % 2 == 0:
        logger.info(number)

# for i in range(0,101,2):
#     print(i)        