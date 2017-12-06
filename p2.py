print("Let's play a game.")
print("If you can guess what number I am thinking, you win absolutely nothing!")
n = input()
from secrets import randbelow
print (randbelow(100))
if n < 'randbelow':
    print("You aimed too low")
elif n > 'randbelow' :
    print("You aimed too high.")
