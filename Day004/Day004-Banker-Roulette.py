# Banker Roulette -- who pay the bill
import random   # put this on top of program
names_string=input("Give me everybody's names, separated by a comma. ")
names=names_string.split(",")
length=len(names)
# print(names)
ran_num=random.randint(0,length-1)
person=names[ran_num]
print(person,"is going to buy the meal today!")

