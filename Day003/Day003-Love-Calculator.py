print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

str=name1.lower()+name2.lower()
t=str.count('t')
r=str.count('r')
u=str.count('u')
e=str.count('e')
true=t+r+u+e
l=str.count('l')
o=str.count('o')
v=str.count('v')
e=str.count('e')
love=(l+o+v+e)
total=(true*10)+love
if total<10 or total>90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total>=40 and total<=50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
