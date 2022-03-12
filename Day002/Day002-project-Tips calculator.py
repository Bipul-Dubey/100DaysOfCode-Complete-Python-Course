# bills payment calculator with tips
print("Welcome to the tip calculator.")
bills=float(input("What was the total bill? "))
tips=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
tip_perc=tips/100
tips_pay=bills*tip_perc
total_pay=bills+tips_pay
final_pay=round(total_pay/people,2)
print(f"Each person should pay: {final_pay}")