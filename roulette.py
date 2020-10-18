import random

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
           18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
           33, 34, 35, 36]
reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34,
        36]
blacks = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31,
          33, 35]
green = [0]

winning_number = random.randint(0, 37)

player_balance = int(input("Please make a deposit(MAX = 500 credits): "))

print("Your balance is {} credits.".format(player_balance))

bets = int(input("Please choose bet value per number: "))
print("Bets are {} credit(s) per number.".format(bets))

choices = list(map(int, input("Choose your numbers: ").split()))

print()

while player_balance > 0:
    bet = len(choices) * bets
    player_balance -= int(bet)
    winning_number = random.randint(0, 37)

    if winning_number in choices:
        print("Congratulations, you win!!!")
        player_balance += 36 * bets
    else:
        print("Sorry, you lose.")

    if winning_number in reds:
        print("The winning number is {} red.".format(winning_number))
    elif winning_number in blacks:
        print("The winning number is {} black.".format(winning_number))
    else:
        print("The winning number is 0 green.")
    if player_balance == 0:
        print("Your balance is too low. Please make a deposit.")
        break

    print()
    print("Current balance is {} credits".format(player_balance))
    bets = int(input("Please choose bet value per number: "))
    print("Bets are {} credit(s) per number.".format(bets))
    choices = list(map(int, input("Choose your numbers: ").split()))
