"""
This program is my submission for MGTC28 in-class exercise #4.
nerve_of_steel.py lets the user set up the Nerve of Steel party game.
Functionality to track the status of players during the game is currently broken.
nerve_of_steel.py uses the time library to help keep track of time
"""


import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images 
import random


#initialize game
number_players = 0
while number_players <= 0:
    number_players = int(input("Please input the number of players: "))
    if number_players <= 0:     #add failsafes for other incorrect inputs
        print("At least one player is needed to play this game.")
print("Great! Now let's keep track of everyone playing the game.")

players_status = {}
while len(players_status) < number_players:
    player_name = str(input("Please input the name of a player: "))     #add unique text for first and last players
    if player_name not in players_status.keys():
        players_status[player_name] = "stand"       #players should be sitting; this is just for convenience
    else:
        print("There is already a player with that name.")

print("Hello players, Welcome to Nerve of Steel!")      #add list of all player names for a more personalized intro"
str(input("To start, all players must sit in a circle. When you're ready, type anything to start the game: "))

round_number = 1
final_winner = "N/A"
im = Image.open("times-up.jpeg")

while final_winner == "N/A":
    print("Round " + str(round_number))
    print("Players stand")
    sitting_players = []
    sleep_time = random.randint(5, 25)
    
    while time.sleep(sleep_time) == True:   #can't change anything while program is sleeping
        for player in players_status:
            if players_status[player] == 'sit' and player not in sitting_players:
                sitting_players.append(player)
    
    im.show()
    print("Time up. Last to sit down wins.")
    print("Players eliminated: ")
    for player in players_status:
        if players_status[player] == 'stand':
            print(player)
            del players_status[player]      #error cuz of changed dictionary size
    print("")       #add dividers n stuff to make the text more readable
    print(sitting_players[len(sitting_players) - 1] + ", you win this round!")      #add failsafe in case nobody wins a round + round specific text

    if len(sitting_players) > 1:
        round_number = round_number + 1
        str(input("Round over. Please input anything to move onto the next round: "))
    elif len(sitting_players) == 1:
        final_winner = sitting_players[0]
    else:
        final_winner = "nobody"

if final_winner != "nobody":
    print(final_winner + ", you win the game!")
else:
    print("all players have been eliminated, better luck next time!")





