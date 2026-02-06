from loguru import logger

labour_name = ["Maheh","Rameh","Mithileh","Sumeh",500,400,400,300]

nums = [2,5,23,78,257,21,43,50000,312]

nums.sort(reverse=True)

logger.info(nums)

# logger.info(labour_name)

# labour_name[0:4] = ["Mahesh","Ramesh","Mithilesh","Sumesh"]

# # labour_name[0:4] = ["Mahesh"] >> o/p: ['Mahesh', 500, 400, 400, 300]

# logger.info(labour_name)

# del labour_name

# logger.info(labour_name) >> gives error as list is deleted >> NameError: name 'labour_name' is not defined

# labour_name.remove(400)

# labour_name.remove(1000) >> gives ValueError: list.remove(x): x not in list

# logger.info(labour_name)

# print(labour_name.pop(2))

# wage = labour_name.pop()

# if wage>200:
#     print("Costly labour charge")

# labour_name.insert(4,"Ram")

# labour_name.append(600)

# logger.info(labour_name)

# new_labour=["Ram","Mahesh"]

#labour_name.append(new_labour) >> o/p is  ['Mahesh', 'Ramesh', 'Mithilesh', 'Sumesh', ['Ram', 'Mahesh']]

# labour_name = labour_name + new_labour #same as extend function

# print(labour_name)

# logger.info(labour_name[1:]) >> second element onwards

# logger.info(labour_name[0:2]) >> first two elements

# logger.info(labour_name[15:]) >> querying out of bounds indices

# logger.info(labour_name[::-1]) >> reverse a list

# logger.info(len(labour_name))

# api_endpoint = "https://portal.azure.com/VMINSTANCE/test-vm/subs_id/aexy-234-mns/getCredential"

# new_api_list = api_endpoint.split('/')

# logger.info(new_api_list)

# logger.info(new_api_list[-2])

