import random
computer=random.randint(0,2)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player=int(input("0 for rock\n1 for paper\n2 for scissors\nwhat you choose?: "))
if player==0 and computer==1:
    print("Your choice: ")
    print(rock)
    print("Computer choice: ")
    print(paper)
    print("You lose")
elif player==1 and computer==0:
    print("Your Choice: ")
    print(paper)
    print("Computer Choice: ")
    print(rock)
    print("You Win")
elif player==0 and computer==2:
    print("Your choice: ")
    print(rock)
    print("Computer choice: ")
    print(scissors)
    print("You Win")
elif player==2 and computer==0:
    print("Your Choice: ")
    print(scissors)
    print("Computer Choice: ")
    print(rock)
    print("You lose")
elif player==1 and computer==2:
    print("Your Choice: ")
    print(paper)
    print("Computer Choice: ")
    print(scissors)
    print("You lose")
elif player==2 and computer==1:
    print("Your Choice: ")
    print(scissors)
    print("Computer Choice: ")
    print(paper)
    print("You Win")
elif player==computer:
    print("Draw")
else:
    print("Wrong Choice")