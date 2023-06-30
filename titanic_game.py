import string


#sg
#create class luck
class Luck:
  def __init__(self, age, equi):
    set_luck_age = {100:list(range(20)), 75:list(range(40, 80)), 50:list(range(20, 40)), 25:list(range(80, 99))}
    for k, v in set_luck_age.items():
      if age in v:
        self.value_age = k
    set_luck_equi = {100:list(string.ascii_lowercase)[:6], 75:list(string.ascii_lowercase)[6:12], 50:list(string.ascii_lowercase)[12:18], 25:list(string.ascii_lowercase)[18:]}
    for k, v in set_luck_equi.items():
      if equi.strip()[0] in v:
        self.value_equi = k
    self.value_age_new = self.value_age
    self.value_equi_new = self.value_equi
    self.value = self.value_age_new + self.value_equi_new
#method for change equi
  def change_eq(self, equiment):
    set_luck_equi = {100:list(string.ascii_lowercase)[:6], 75:list(string.ascii_lowercase)[6:12], 50:list(string.ascii_lowercase)[12:18], 25:list(string.ascii_lowercase)[18:]}
    for k, v in set_luck_equi.items():
      if equiment.name.strip()[0] in v:
        self.value_equi = k
        self.value_equi_new = self.value_equi
        self.value = self.value_age_new + self.value_equi_new
#method when upgrade equi
  def update_eq(self, equiment):
    luck_level_eq = {"bronze":0.25, "siver":0.35, "gold":0.5, "platinum":0.7}
    for k, v in luck_level_eq.items():
      if k == equiment.level:
        self.value_equi_new += (v * self.value_equi)
        self.value = self.value_age_new + self.value_equi_new
#method when upgrade age
  def update_age(self, player):
    luck_level_age = {1:list(range(20)), 0.75:list(range(40, 80)), 0.5:list(range(20, 40)), 0.25:list(range(80, 99))}
    for k, v in luck_level_age.items():
      if player.age in v:
        self.value_age_new += (k * self.value_age)
        self.value = self.value_age_new + self.value_equi_new
#describe class
  def __repr__(self):
    return "Now you have {} luck value.".format(self.value)


#create class equiment
class Equiments:
  def __init__(self, name, level="bronze"):
    self.name = name
    self.level = level
#method when upgrade equi
  def upgrade_level(self):
    level_Eq = {1:"bronze", 2:"siver", 3:"gold", 4:"platinum"}
    if self.level != "platninum":
      for k, v in level_Eq.items():
        if self.level == v:
          m = k+1
          self.level = level_Eq.get(m)
    else:
      pass
#describe class
  def __repr__(self):
    return "{} have {} level".format(self.name, self.level)

  
#create class player
class Player:
  def __init__(self, name, age, equiment):
    self.name = name
    self.age = age
    self.equiments = Equiments(equiment)
    self.luck = Luck(age, equiment)
#method when added age
  def added_age(self):
    self.age += 1
#method when change equi
  def update_equiment(self, pick):
    self.equiments = Equiments(pick)
#describe class
  def __repr__(self):
    return "{name} is a player of TITANIC game is {age} years old. {name} have {equi} ({equi_le}) and have luck at {luck}.".format(name=self.name, age=self.age, equi=self.equiments.name, equi_le=self.equiments.level, luck=self.luck.value)


#create class titanic
class Game:
  titanic = 100
  survive = 0
  def __init__(self, name):
    self.player = name
  def will_sink(self, luck):
    sink = 5
    sink -= sink * (luck/200)
    self.titanic -= sink
  def will_survive(self, luck):
    survive_v = 5
    survive_v += survive_v * (luck/200)
    self.survive += survive_v
  def check_status(self):
    if (self.titanic >= 30) & (self.survive < 75):
      return "continue"
    elif self.titanic < 30:
      return "lose"
    elif self.survive >= 75:
      return "win"


# function playgame
import random
def get_user_choice(player):
    valid_choices = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("{}! Enter your choice (rock/paper/scissors): ".format(player.name)).lower()
        if user_choice in valid_choices:
            return user_choice
        print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    print(f"Computer chose {computer_choice}.\n")
    if user_choice == computer_choice:
        return "upgrade"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "survive"
    else:
        return "sink"

#when start game!!
def start_game():
  num = int(input("\nWelcom! to TITANIC GAME\nNumber of Player?\n"))
  players = []
  game_players = []
  for i in range(num):
    name, age, equi = input(f"player{i+1}: ").split()
    age = int(age)
    players.append(Player(name, age, equi))
    game_players.append(Game(name))
  return players, game_players

#do something from result
def action_from_result(result, game, player):
  if result == "survive":
    game.will_survive(player.luck.value)
  elif result == "sink":
    game.will_sink(player.luck.value)
  else:
    player.update_equiment(input(f"{player.name} can choose new equiment\n").strip())
    #update luck after change euqiment
    player.luck.change_eq(player.equiments)

#play game

#ask number of player and input player and detail
players, game_players = start_game()
#loop 3 round meaning total 9 round
for _ in range(3):
  #play game 3 round.
  for _ in range(3):
    #loop in each players.
    for i in range(len(players)):
      #show current status.
      print(f"\nstatus of {players[i].name} \ntitanic: {game_players[i].titanic} \nsurvive: {game_players[i].survive}\n")
      #play RPS and save result.
      result = determine_winner(get_user_choice(players[i]), get_computer_choice())
      #do actioin from result.
      action_from_result(result, game_players[i], players[i])
      #show status after play 1 round
      print(f"At now!! status of {players[i].name} \ntitanic: {game_players[i].titanic} \nsurvive: {game_players[i].survive}")
      #show ending 1 round for all players
      print(f"Ending {players[i].name} round.\n")
    #show datial in each player after 1 round
    for i in range(len(players)):
      print(players[i])
  #loop all players
  for i in range(len(players)):
    #upgrade equiments after 3 round
    players[i].equiments.upgrade_level()
    #update luck after upgrade euqiment
    players[i].luck.update_eq(players[i].equiments)
#loop all players
for i in range(len(players)):
  #update age after 9 round
  players[i].added_age()
  players[i].luck.update_age(players[i])