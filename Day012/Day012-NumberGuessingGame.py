logo="""
  _   _                 _                  _____                     _             
 | \ | |               | |                / ____|                   (_)            
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` |
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| |
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |
                                                                              __/ |
                                                                             |___/ 
"""
easy_level_lives=10
hard_level_lives=5

def guess():
    import random
    return random.randint(1,100)

def easy_level():
    global easy_level_lives
    guess_num=guess()
    while easy_level_lives:
            num=int(input("Make your guess: "))
            if num==guess_num:
                print(f"You got it. Right answer was {guess_num}")
                break
            else:
                if num<guess_num:
                    print("Guess number is low")
                else:
                    print("Guess number is high")
                easy_level_lives-=1
            print(f"You have {easy_level_lives} lives left.")
            if easy_level_lives == 0:
                print("----hahaha you lose it looser----")


def hard_level():
    global hard_level_lives
    guess_num=guess()
    while hard_level_lives:
        num=int(input("Make your guess: "))
        if num==guess_num:
            print(f"You got it. Right answer was {guess_num}")
            break
        else:
            if num<guess_num:
                print("Guess number is low")
            else:
                print("Guess number is high")
            hard_level_lives-=1
        print(f"You have {hard_level_lives} lives left.")
        if hard_level_lives == 0:
            print("----hahaha you lose it looser----")

def choose_level():
    level_chosen=input("Choose a difficulty level. Type 'easy' or 'hard'. ").lower()
    if level_chosen=='easy':
        easy_level()
    elif level_chosen=='hard':
        hard_level()
    else:
        print("Please your level.")


print("Welcome to the Number guessing Game.")
print("Guess a number between 1-100")
game_run=True
while game_run==True:
    start=input("Do you want to play??..Type 'y' to play or 'n' to exit..")
    if start=='y':
        print(logo)
        choose_level()
    elif start=='n':
        game_run=False

