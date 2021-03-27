import random

random.randint(0, 10)

team_1_rank = 1
team_1_name = "Sharks"
team_2_rank = 16
team_2_name = "Hot-dogs"

def success_calcualtor(x):
  x = 100 / x 
  return x 

team_1_success = success_calcualtor(team_1_rank)
team_2_success = success_calcualtor(team_2_rank)

team_1_win_chance = team_1_success + random.randint(0, 100)
team_2_win_chance = team_2_success + random.randint(0, 100)

if team_1_win_chance > team_2_win_chance:
  print(f"{team_1_name} wins!")
  print(f"{team_1_name} change was {team_1_win_chance}")
  print(f"{team_2_name} change was {team_2_win_chance}")
  
else:
  print(f"{team_2_name} wins!")
  print(f"{team_1_name} change was {team_1_win_chance}")
  print(f"{team_2_name} change was {team_2_win_chance}")