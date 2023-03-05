print ("...rock...\n...paper...\n...scissor...")
player1 = input("Player one chooses: ")
player2 = input("Player two chooses: ")

if player1 == "rock" and player2 == "scissor":
    print("Player 1 wins")
elif player1 == "rock" and player2 == "paper":
    print("Player 2 wins")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins") 
elif player1 =="paper" and player2 =="scissor":
    print("Player 2 wins")
elif player1 == "scissor" and player2 == "paper":
    print("Player 1 wins")
elif player1 == "scissor" and player2 == "rock":
    print("Player 2 wins")
elif player1 == player2:
    print("Tie")
else:
    print("something went wrong")