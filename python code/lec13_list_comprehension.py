# new_list=[]
# for i in range(1,11):
#     if i % 2 == 0:
#         new_list.append(i)

# print(new_list)

# new_list=[i for i in range(1,11) if i % 2 == 0]

# print(new_list)

new_list=[]
for i in range(1,11):
    if i % 2 == 0:
        new_list.append('Even')
    else:
        new_list.append('Odd')

print(new_list)

new_list = ['Even' if i%2==0 else 'Odd' for i in range(1,11)]

print(new_list)