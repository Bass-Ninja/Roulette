import random

reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
blacks = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green = [0]

winning_number = random.randint(0, 37)

valid_choices = list(map(int, input("Choose your numbers:").split()))

print()

if winning_number in valid_choices:
    print("Congratulations, you win!!!")
else:
    print("Sorry, you lose.")


if winning_number in reds:
    print("The winning number is {} red.".format(winning_number))
elif winning_number in blacks:
    print("The winning number is {} black.".format(winning_number))
else:
    print("The winning number is 0 green.")
