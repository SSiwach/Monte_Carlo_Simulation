import random # to import random number generator

import matplotlib

import matplotlib.pyplot as plt

def rollDice(): #Defining a function roll Dice
  roll = random.randint(1,100)

  if roll == 100:
    return False
  elif roll <= 50:
    return False
  elif 100 > roll > 50:
    return True

def doubler_bettor(funds, initial_wager, wager_count):
  value = funds
  wager = initial_wager

  wX = []
  vY = []

  currentWager = 1
  previousWager = 'win'
  previousWagerAmount = initial_wager

  while currentWager <= wager_count:
    if previousWager == 'win':
      print('we won the last wager, great')
      if rollDice():
        value += wager
        print(value)
        wX.append(currentWager)
        vY.append(value)
      else:
        value -= wager
        previousWager = 'loss'
        print(value)
        previousWagerAmount = wager
        wX.append(currentWager)
        vY.append(value)
        if value < 0 :
          print('we went broke after'.currentWager,'bets')
          #currentWager += 100000000000000
          break
    elif previousWager == 'loss':
      print('We lost the last one, so we will be smart and double')
      if rollDice():
        wager = previousWagerAmount*2
        print('we won', wager)
        print(value)
        wager = initial_wager
        previousWager = 'win'
        wX.append(currentWager)
        vY.append(value)

      else:
        wager = previousWagerAmount *2
        print('we lost', wager)
        value -= wager
        if value < 0 :
          print('we went broke after', currentWager,'bets')
          #currentWager += 100000000000000
          break
        
        print(value)
        previousWager ='loss'
        wX.append(currentWager)
        vY.append(value)
        


    currentWager +=1

  print(value)
  plt.plot(wX, vY)

doubler_bettor(10000,100,100)

plt.show()



