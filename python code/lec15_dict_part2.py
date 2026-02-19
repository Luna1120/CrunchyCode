
labour_with_cost = {"Mahesh":500,"Ramesh":400,"Mithilesh":400,"Sumesh":300}   

labour_with_cost["Jagmohan"] = 1000

labour_with_cost["Rampyare"] = 800

# Get method
# print(labour_with_cost.get("Mahesh1"))
# print(labour_with_cost["Mahesh"])

# Keys and Values
# print(labour_with_cost.keys())
# print(labour_with_cost.values())

# Item Method
# print(labour_with_cost.items())

# Update method
# labour_with_cost.update({"manish":700,"ram":800})
# print(labour_with_cost)
# new_dict = {"manish":700,"ram":900}
# final_dict = {**labour_with_cost,**new_dict}
# print(final_dict)

#Pop method
# print(labour_with_cost)
# print(labour_with_cost.pop("Mahesh"))
# print(labour_with_cost.popitem())
# print(labour_with_cost.popitem())
# print(labour_with_cost.keys())

# Copy method
# new_labour_cost = labour_with_cost.copy()
# print(id(labour_with_cost))
# print(id(new_labour_cost))

# Clear method
# labour_with_cost.clear()
# print(labour_with_cost)

# Dictionary comprehension
# labour_with_cost = {key:labour_with_cost.get(key)+100
#                      for key in labour_with_cost}
# print(labour_with_cost)
# labour_with_cost = {key:labour_with_cost.get(key)+100 if key!= 'Jagmohan' 
#                     else labour_with_cost.get(key)
#                     for key in labour_with_cost}
# print(labour_with_cost)

name = 'Manas'

letter_count = {}
for char in name:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1
    # print(letter_count)
print(letter_count)

