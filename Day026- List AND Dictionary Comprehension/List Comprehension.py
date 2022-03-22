# working with list
## general method
# list1=[1,2,3,4,5]
# new_list=[]
# for n in list1:
#     add_1=n+1
#     new_list.append(add_1)
# print(new_list)

# by using list comprehension
# new_list=[new_item for item in list]
# list2=[2,3,4,5,6]
# new_list=[item+1 for item in list2]
# print(new_list)


# string comprehension
# name="himanshu"
# letter_list=[letter for letter in name]
# print(letter_list)

# num_list=[item*2 for item in range(1,5)]
# print(num_list)

# conditional list comprehension
# new_list=[new_item for item in list if test_condition]

names=['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
new_names=[name.upper() for name in names if len(name)>=5]
print(new_names)