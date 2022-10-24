import random
print("Welcome To Snake,Water,Gun Game!")
round = int(input("How Much Rounds Do You Want To Play? : "))
i = 1
u_score = 0
c_score = 0
while (i<round+1):
  print ("\nRound",i,"!  ||  Score Panel : ")
  print("               Computer's Score : ",c_score)
  print("               Your Score : ",u_score)
  c_guees = random.randint(1,3)
  if (c_guees == 1):
    ac_guees = "s"
  elif (c_guees == 2):
    ac_guees = "w"
  elif (c_guees == 3):
    ac_guees = "g"
  print("\nComputer has chosen, now its your turn")
  u_guees = input("Snake , Water , Gun Choose One -> (S) (W) (G) : ")
  i += 1
  if (ac_guees == "s" and u_guees == "s" or ac_guees == "w" and u_guees == "w" or ac_guees == "g" and u_guees == "g"):
    print ("It's a Tie")
    u_score += 10
    c_score += 10
    continue
  elif (u_guees == "s" and ac_guees == "w" or u_guees == "w" and ac_guees == "g" or u_guees == "g" and ac_guees == "s"):
    print("You Won This Round!")
    u_score += 10
  elif (u_guees == "s" and ac_guees == "g" or u_guees == "w" and ac_guees == "s" or u_guees == "g" and ac_guees == "w"):
    print("Ooo! You Lost This Round")
    c_score += 10
  else:
    print("Enter a Valid Input!")
    i -= 1
print("\nThe Final Score : ")
print("Your Score : ",u_score)
print("Computer's Score : ",c_score)
if (u_score>c_score):
  diff = (u_score-c_score)
  print("Congratulations! You Won By",diff,"Runs!\nWell Played!!!")
elif (c_score>u_score):
  diff = (c_score-u_score)
  print("Ooooo! You Lost By",diff,"Runs!")
elif (u_score == c_score):
  print("This Game was a Tie!")
# Finally Done!
