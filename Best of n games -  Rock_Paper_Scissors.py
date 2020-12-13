import random
import math


def rps():
    user=input("What's your choice ? 'r'for rock,'p'for papper and 's' for scissors: ")
    user=user.lower()
    
    if user not in ('r','p','s'):
        print("Wrong choice, type a following letter 'r','p' or 's'")

    computer = random.choice(['r','p','s'])

    if user ==computer:
        return(0,user,computer)


    if win(user,computer):
        return(1,user,computer)

    return (-1,user,computer)


def win(user,computer):
    if (user=='r' and computer=='s') or (user=='p' and computer=='r' ) or (user=='s' and computer=='p'):
        return True
    return False


def best_of(n):
	#playing againts  the computer in the best of n games 
	#to win, you must win (n/2) games (exp (2 out 3) or (3 out 5) games)
	n=int(input("Enter who many games you want to play: "))
	player_wins=0
	computer_wins=0
	wins_necessary =math.ceil(n/2)
	while player_wins < wins_necessary and computer_wins <wins_necessary:
		result,user,computer=rps()
		#tie
		if result==0:
			print(f'It is a tie. The user and the computer have both chose {user}')
		#if you won
		elif result==1:
			player_wins+=1
			print(f'You chose {user} and the computer chose {computer}. You won!')

		else:
			computer_wins+=1
			print(f'You chose{user} and the coumputer chose {computer}. You lost!')


	if player_wins>computer_wins:
		print(f'You have won the best of {n} games')
	else:
		print(f'Unfortunately,thr computer has won the best of {n} of games')


best_of('n')
