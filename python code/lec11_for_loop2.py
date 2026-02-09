from loguru import logger

# paragraph = """ Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
# data warehouse and business intelligence industry’s thought leader on the dimen
# sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
# books written by Ralph and his colleagues have been the industry’s best sellers 
# since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
# coinvented the Star workstation, the fi rst commercial product with windows, icons, 
# and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
# electrical engineering from Stanford University """

# paragraph_lst = paragraph.lower().split(" ") # if we put lower at end, gives error >> list object 
# # has no attribute lower hence paragraph.lower() as lower is a string method

# print(paragraph_lst)

# count = 0

# for word in paragraph_lst:
#     if word == 'the':
#         count+=1
#     else:
#         continue

# logger.info(f"Total count for 'the' article is {count}")

#Assignment 2

# I have a sorted list and need to insert the new value in such a way that after inserting the element
# list will be sorted.

list1 = [5,18,77,108,930]
number_to_insert = 1

index = 0

for number in list1:
    if number > number_to_insert:
        index=index
        break
    else:
        index += 1

list1.append(None)

for i in range(len(list1)-1,index,-1):
    list1[i] = list1[i-1]

list1[index] = number_to_insert

logger.info(f"Final list is {list1}")
