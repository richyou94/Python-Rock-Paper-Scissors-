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

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

match user_choice:
    case "0":
        user_choice = "rock"
        print(rock)
        print("You choose: ")
    case "1":
        user_choice = "paper"
        print(paper)
        print("You choose: ")
    case "2":
        user_choice = "scissors"
        print(scissors)
        print('You choose: ')

imageChoices = [rock, paper, scissors]
listOfChoices = ["rock", "paper", "scissors"]
randomNumber = random.randint(0, 2)
computer_choice = listOfChoices[randomNumber]
print(imageChoices[randomNumber])
print("Computer choose: ")



if user_choice == computer_choice:
    print("Draw!")
elif user_choice == "rock" and computer_choice == "paper":
    print('You lose!')
elif user_choice == "rock" and computer_choice == "scissors":
    print('You win!')
elif user_choice == "paper" and computer_choice == "rock":
    print('You win!')
elif user_choice == "paper" and computer_choice == "scissors":
    print('You lose!')
elif user_choice == "rock" and computer_choice == "paper":
    print("You lose!")
elif user_choice == "rock" and computer_choice == "scissors":
    print('You win!')


