import time
 
Gryffindor = 0
Hufflepuff = 0
Ravenclaw = 0
Slytherin = 0
 
while True:
    light = input('Q1) Do you like Dawn or Dusk?\n  1) Dawn\n  2) Dusk\n  :')
 
    if light in ['1','2']:
        light = int(light)
        break
    else:
         print("pick one of the numbers silly")
    time.sleep(2)
 
 
if light == 1: 
    Gryffindor += 1
elif light == 2:
    Hufflepuff += 1
    Slytherin += 1
 
while True:
    dead = input("Q2) When I'm dead, I want people to remeber me as\n  1) The Good\n 2) The Great\n 3) The Wise\n 4) The Bold\n :")
 
    if dead in ['1','2','3','4']: 
        dead = int(dead)
        break
    else:
        print('pick a number dummy')
    time.sleep(2)
 
if dead == 1:
    Hufflepuff += 2
elif dead == 2:
    Slytherin += 2
elif dead == 3:
    Ravenclaw += 2
elif dead == 4:
    Gryffindor += 2
 
while True:
    ear = input("Q3) Which kind of instrument most pleases your ear?\n 1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum\n :")
 
    if ear in ['1','2','3','4']:
        ear = int(ear)
        break
    else:
        print('do i rlly have to keep telling you..')
    time.sleep(2)
 
if ear == 1:
    Slytherin += 4
elif ear == 2:
    Hufflepuff += 4
elif ear == 3:
    Ravenclaw += 4
elif ear == 4: 
    Gryffindor += 4
 
print('okay here are the results..')
 
time.sleep(1)
 
if Slytherin > Hufflepuff:
    print('Your a Slytherin')
elif Hufflepuff > Slytherin:
    print('Your a Hufflepuff')
elif Ravenclaw > Gryffindor:
    print('Your a Ravenclaw')
elif Gryffindor > Ravenclaw:
    print('Your a Gryffindor')