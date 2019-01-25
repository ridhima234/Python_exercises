
status=True
while(status):
	pl1=str(input("Enter player1 turn"))
	pl2=str(input("Enter player2 turn"))
    if pl1=="Rock" and pl2=="Scissors" or pl1=="Scissors" and pl2=="Rock":
        print("Rock beats Scissors")
        status=False
    elif pl1=="Scissors" and pl2=="Paper" or pl1=="Paper" and pl2=="Scissors":
        print("Scissors beats paper")
        status=False
    elif pl1=="Paper" and pl2=="Rock" or pl1=="Rock" and pl2=="Paper":
        print("Paper beats Rock")
        status=False
    elif pl1=="Rock" and pl2=="Rock" or pl1=="Paper" and pl2=="Paper" or pl1=="Scissors" and pl2=="Scissors" :
        print("No one wins")