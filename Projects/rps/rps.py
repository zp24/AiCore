

#num_list = [5, 7, 8, 9, 22, 55, 99, 100000]

import time
import random
#print(random.choice(num_list)) #will print a random number from list

#def shout(text): 
 #   return text.upper() 
#print(shout('Hello'))

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    #print("stop")

player_continue = True

def main(): 
    player_continue
win = 0
loss = 0
draw = 0
while player_continue:
    
    gesture = ["rock", "paper", "scissors"]
    computer_choice = random.choice(gesture)

    
    player_choice = input("Choose rock, paper, or scissors: ")
    
    choices = "Computer chose: " + computer_choice + " // " + "Player chose: " + player_choice
    game_end = "Game ended\n" + "Your Stats: " + "Wins: "+ str(win) + " Losses: " + str(loss) + " Draws: " + str(draw)
    
    if computer_choice == player_choice: 
            draw += 1 #adds 1 to the overall number of draws
            print(choices)
            print("It's a draw", "\nWins: ", win, "Losses: ", loss, "Draws: ", draw) #shows stats
            continue
    elif computer_choice == "rock" and player_choice == "paper" or computer_choice == "scissors" and player_choice == "rock" or computer_choice == "paper" and player_choice == "scissors":
            win += 1 #adds 1 to the overall number of wins
            print (choices)
            print("Player wins!", "\nWins: ", win, "Losses: ", loss, "Draws: ", draw) #shows stats
            continue
    elif computer_choice == "paper" and player_choice == "rock" or computer_choice == "rock" and player_choice == "scissors" or computer_choice == "scissors" and player_choice == "paper":
            loss += 1 #adds 1 to the overall number of losses
            print(choices)
            print("Computer wins!", "\nWins: ", win, " Losses: ", loss, "Draws: ", draw) #shows stats
            continue
    else:
            if player_choice == "x": #press x to quit game
                player_continue = False #breaks loop
                print(game_end) #confirm loop has broken
            break
 #   else:
  #      print("dud")
main()


#countdown(5)

#test = countdown(5)

#if test == countdown(0):
 #   print("this is working")
#else:
 #   print("dud")