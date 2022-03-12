logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
def highest_bids(bids):
    max_bid=0
    for bidder in bids:
        bid_amount=bids[bidder]
        if bid_amount>max_bid:
            max_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid amount of {max_bid}")

bid_info = {}
go_on = True
while go_on:
    name=input("Enter your name: ")
    bit_amount=int(input("what is your bit amount?? $"))
    bid_info[name]=bit_amount
    run=input("Are there any other bidders??? 'yes' to continue otherwise 'no' -> ").lower()
    if run=='no':
        go_on=False
        highest_bids(bid_info)
    elif run=='yes':
        #clear()
        pass
