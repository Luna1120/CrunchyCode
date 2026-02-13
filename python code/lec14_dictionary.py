from loguru import logger
# print("Programming aasan hai!")

labour_with_cost = {"Mahesh":500,"Ramesh":400,"Mithilesh":400,"Sumesh":300}   

labour_with_cost["Jagmohan"] = 1000

labour_with_cost["Rampyare"] = 800

# logger.info(labour_with_cost)

# logger.info(labour_with_cost.keys())
# logger.info(labour_with_cost.values())
# logger.info(labour_with_cost.items())

logger.info(labour_with_cost["Mithilesh"])

for name in labour_with_cost:
    # logger.info(name,labour_with_cost[name]) --> logger.info only gives first key value, we need to put in f""
    logger.info(f"{name},{labour_with_cost[name]}")

for key,value in labour_with_cost.items():
    # logger.info(key,value) --> logger.info only gives first key value, we need to put in f"" for full output
    logger.info(f"{key},{value}")