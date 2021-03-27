import random
import decimal
import time

random.randint(0, 10)

team_1_rank = 12
team_1_name = "Sharks"
team_2_rank = 16
team_2_name = "Hot-dogs"

def success_calcualtor(x):
  x = 100 / x 
  return x 

team_1_success = success_calcualtor(team_1_rank)
team_2_success = success_calcualtor(team_2_rank)

team_1_win_chance = (team_1_success * (random.randint(0, 10) / 100)) * 100
team_1_win_chance = round(team_1_win_chance, 2)
team_2_win_chance = (team_2_success * (random.randint(0, 10) / 100)) * 100
team_2_win_chance = round(team_2_win_chance, 2)

print("We are calculating chances...")

time.sleep(2)

print("...working on it...")

time.sleep(2)

if team_1_win_chance > team_2_win_chance:
  print(f"{team_1_name} wins!")
  print(f"{team_1_name} chance was {team_1_win_chance}%")
  print(f"{team_2_name} chance was {team_2_win_chance}%")
else:
  print(f"{team_2_name} wins!")
  print(f"{team_1_name} chance was {team_1_win_chance}%")
  print(f"{team_2_name} chance was {team_2_win_chance}&")