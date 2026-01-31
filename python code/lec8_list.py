from loguru import logger

# labour_name = ["Mahesh","Ramesh","Mithilesh","Sumesh"]

# logger.info(f"First element in the list is {labour_name[-1]}")

# # labour_name.append("Ram")

# # labour_name.append("Mohan")

# # labour_name.insert(2,"Ram")

# new_labour=["Ram","Mahesh"]

# labour_name.extend(new_labour)

# # logger.info(f"First element in the list is {labour_name}")

labour_with_wage = [["mahesh",500],["ramesh",400]]

logger.info(f"Labour {labour_with_wage[1][0]} is charging total of {labour_with_wage[1][1]} per day")