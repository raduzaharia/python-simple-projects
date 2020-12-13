'''
The Rules of the rock-paper-scissors are:
Rock > Scissors , Paper > Rock , Scissors >Paper
If both choice the same (Rock=Rock,Paper=Paper  Scissors=Scissors) the result is a tie . 
'''
#using if/elif statements
import random

user=input("What's your choice ? 'r'for rock,'p'for papper and 's' for scissors: ")
user=user.lower()
computer = random.choice(['r','p','s'])


if user =="r" and computer =="r":
                print("It's a tie")
elif user=="r" and computer =="p":
                print("You won")
elif user=="r" and computer=="s":
                print("You lost")

if user =="p" and computer =="p":
                print("It's a tie")
elif user=="p" and computer =="r":
                print("You won")
elif user=="p" and computer=="s":
                print("You lost")
		
if user =="s" and computer =="s":
                print("It's a tie")
elif user=="s" and computer =="p":
                print("You won")
elif user=="s" and computer=="r":
                print("You lost")
                
#------------------------------------------------------------------------------
#using functions and if/elif statements

import random

def rps():
	user=input("What's your choice ? 'r'for rock,'p'for papper and 's' for scissors: ")
	user=user.lower()
	computer = random.choice(['r','p','s'])

	if user ==computer:
		return("It's a tie")

	if win(user,computer):
		return('You won')

	return ("You lost")


def win(user,computer):
    if (user=='r' and computer=='s') or (user=='p' and computer=='r' ) or (user=='s' and computer=='p'):
        return True

print(rps())
