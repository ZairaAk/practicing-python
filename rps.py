import random
options = ["rock", "paper", "scissors"]
player_score=0
computer_score=0   


while True:
    player=input("Choose Rock Paper Scissors")
    computer = random.choice(options)
    print(f"Computer chose: {computer}")
        
    if player==computer:
        print("It's a tie!")
    elif player== "rock" and computer == "scissors":
        print("You win!")
        player_score += 1
    elif player== "scissors" and computer == "paper":
        print("You win!")   
        player_score += 1 
    elif player== "paper" and computer == "rock":
        print("You win!")   
        player_score += 1     
    else:
        print("Computer wins!") 
        computer_score += 1

    print(f"Score => You: {player_score} | Computer: {computer_score}")


    


    again=input("One more round?: y/n")
    if again.lower()!='y':
     break
      
      
        

print(f"Final Score: your score:{player_score} and Computer Score is:{computer_score}")
if(player_score>computer_score):
    print("YOU WIN")
elif(computer_score>player_score):
    print("you lost :( ")
else:
  print("its a tie!")