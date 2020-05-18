from math import fabs
from random import randint
randomizacja=randint(1,100)
print (randomizacja)
print ("Computer picked a number from 1 to 100 you have to Guess it!")
print ("On your first guess computer tells you if you are in 10 range from the number it will say 'WARM', otherwise 'COLD")
print ("On your next guess computer tells you if you are closer than before It will say 'WARMER', otherwise 'COLDER'")
guess =int(input("Make your first guess: "))

odleglosc=fabs(guess-randomizacja)
licznik=0

while (guess!=randomizacja):
  if(licznik==0):
    if(fabs(guess-randomizacja)>10):
      print ("COLD")
    else:
      print ("WARM")
    licznik+=1
    continue
  else:
    guess =int(input("Make a guess: "))
    last=odleglosc
    odleglosc=fabs(guess-randomizacja)
    if(last<odleglosc):
      print("COLDER")
    else:
      print ("WARMER")
    licznik+=1

print("You got it, it took you {} times to guess the number.".format(licznik))


