"""
Ask number of game played in a tournament.Ask the user number of games won and number of games loss. Calculate number of tie and total points. (1 win= 4 points, 1 tei= 2 points)
"""

games_played= int(input("Enter games played"))
games_won= int(input("Enter games won"))
games_loss= int(input("Enter games loss"))

games_tie=games_played-games_won-games_loss
print(f"Games tied = {games_tie}")
total_points=(games_won*4)+(games_tie*2)

print(total_points)
