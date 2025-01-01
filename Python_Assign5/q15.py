''' Modify a script to play 1,000,000 games of craps. Use two dictionaries, wins and losses, to track
 the number of games won and lost for each roll number. Update these dictionaries as the simulation
 progresses. For example, a key–value pair 4: 50217 in the wins dictionary would mean that
 50,217 games were won on the 4th roll. At the end of the simulation, display:
 (i) The percentage of games won.
 (ii) The percentage of games lost.
 (iii) The percentage of games resolved on each roll.
 (iv) The cumulative percentage of games resolved up to each roll.
 Sample Output
 Percentage of wins: 50.2%
 Percentage of losses: 49.8%
 Percentage of wins/losses based on total number of rolls:
 Rolls | % Resolved on this roll | Cumulative % of games resolved-----------------------------------------------------------------
1
 | 30.10%
 2
 ...
 | 20.80%
 | 30.10%
 | 50.90%'''

import random

def play_craps():
    wins = {}
    losses = {}
    total_games = 1000000
    for _ in range(total_games):
        roll_count = 0
        while True:
            roll_count += 1
            roll = random.randint(1, 6) + random.randint(1, 6)
            if roll_count == 1 and roll in (7, 11):
                wins[roll_count] = wins.get(roll_count, 0) + 1
                break
            elif roll_count == 1 and roll in (2, 3, 12):
                losses[roll_count] = losses.get(roll_count, 0) + 1
                break
            # Continue rolling logic here...

    win_percentage = sum(wins.values()) / total_games * 100
    loss_percentage = sum(losses.values()) / total_games * 100
    print(f"Percentage of wins: {win_percentage:.2f}%")
    print(f"Percentage of losses: {loss_percentage:.2f}%")

play_craps()
