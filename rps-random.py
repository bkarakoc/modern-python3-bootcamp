from random import randint 

rock, paper, scissors = 0, 1, 2
computer = randint(0, 2)

0, 1, 2 = rock
player = input("Please enter your move: ")

if player == computer:
    print("It's a tie!")
elif player == "rock":
	if computer == 







# if player1 == player2:
# 	print("It's a tie!")
# elif player1 == "rock":
# 	if player2 == "scissors":
# 		print("player1 wins!")
# 	elif player2 == "paper":
# 		print("player2 wins!")
# elif player1 == "paper":
# 	if player2 == "rock":
# 		print("player1 wins!")
# 	elif player2 == "scissors":
# 		print("player2 wins!")
# elif player1 == "scissors":
# 	if player2 == "paper":
# 		print("player1 wins!")
# 	elif player2 == "rock":
# 		print("player2 wins!")	
# else:
# 	print("something went wrong")
