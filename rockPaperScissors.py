import random

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
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
options = [rock, paper, scissors]

user_input = int(input())
pc_input = random.randint(0, 2)


print(options[user_input])
print("\nComputer chose:")
print(options[pc_input])

if pc_input == user_input:
    print("Draw")
else:
    if pc_input != 0:
        if user_input == pc_input - 1:
            print("You Lose")
        else:
            print("You Win")
    else:
        if user_input == 1:
            print("You Win")
        else:
            print("You Lose")