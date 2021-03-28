import random
import os
import time



print("Hello! Welcome to your not-real bank balance!")
time.sleep(0.5)
if os.path.exists("savedGames.py"):
  print("Found Save file...")
  import savedGames
  n = savedGames.name
  m = savedGames.money
  time.sleep(1)
  print("Name is " +n)
  time.sleep(.3)
  print("You have $"+str(m))
else:
  n = input(str("What is your name?\n"))
  m = random.randint(1, 10000)
  print("Welcome " + n + ", this is your bank balance!")
  print("you have $" + str(m))

  f = open("savedGames" + ".py","w+")
  f.write("name = '"+ n + "'")
  f.write("\nmoney = " + str(m))
  f.close()

time.sleep(1)
auto = 0
while True:
  ch = input(str("type 'get' to get money\nType save to overwrite your last save\n")).lower()
  if (ch == "get"):
    ma = random.randint(5, 50)
    print("you got $"+str(ma))
    m = m + ma
    print("you now have $"+str(m))
    time.sleep(.3)
    auto = auto + 1
  elif (ch == "save"):
    f = open("savedGames" + ".py","w+")
    f.write("name = '"+ n + "'")
    f.write("\nmoney = " + str(m))
    f.close()
    os.system('clear')
    time.sleep(1)
    print("Progress Saved")
    time.sleep(.3)
    auto = 0
    continue
  if(auto == 5):
    f = open("savedGames" + ".py","w+")
    f.write("name = '"+ n + "'")
    f.write("\nmoney = " + str(m))
    f.close()
    auto = 0
    print("Game autosaved to savedGames.py!")
    continue
  
