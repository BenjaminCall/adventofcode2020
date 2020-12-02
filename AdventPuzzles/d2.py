import os

inputs = open(os.getcwd() + '/inputs/d2.txt', 'r') 
lines = inputs.readlines() 

validPass = 0
failedPass = 0
validPass2 = 0
failedPass2 = 0

def isValidP1(mini,maxi,letter,password):
  return password.count(letter) >= mini and password.count(letter) <= maxi

def isValidP2(mini,maxi,letter,password):
  return (password[mini-1] == letter or password[maxi-1] == letter) and password[mini-1] != password[maxi-1]

for line in lines:
    times, letter, password = line.split(' ')
    mini,maxi = times.split('-')
    letter = letter[0]

    if isValidP1(int(mini), int(maxi), letter, password):
      validPass += 1
    else:
      failedPass += 1

    if isValidP2(int(mini), int(maxi), letter, password):
      validPass2 += 1
    else:
      failedPass2 += 1
    
print(validPass)
print(validPass2)
