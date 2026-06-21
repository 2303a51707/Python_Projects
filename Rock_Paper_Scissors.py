import random

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
ROCK'''

paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
PAPER'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
SCISSORS'''
      
you = int(input("What do you want to choose? 0 for rock, 1 for paper, 2 for scissors: "))

if you == 0:
    print(rock)
elif you == 1:
    print(paper)
elif you == 2:
    print(scissors)
else:
    print("Invalid choice!")

computer = random.randint(0,2)

print("Computer chose:")
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

if you == computer:
    print("Match drawn")
elif you == 0 and computer == 2:
    print("You win!")
elif you == 2 and computer == 1:
    print("You win!")
elif you == 1 and computer == 0:
    print("You win")
else:
    print("You lose! Computer won")
