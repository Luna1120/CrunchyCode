from loguru import logger
import time

labour_name = ["Mahesh","Ramesh","Mithilesh","Sumesh"]

# name_iter = 0

# while name_iter < len(labour_name):
#     logger.info(f"{labour_name[name_iter]}")
#     name_iter+=1

# name_iter = len(labour_name)-1

# while (name_iter >= 0):
#     logger.info(f"{labour_name[name_iter]}")
#     name_iter-=1

name_iter = len(labour_name)-1

while (name_iter >= 0):
    logger.info(f"{labour_name[name_iter]}")
    time.sleep(5)
    name_iter-=1

