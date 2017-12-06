echo "# roll" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/amjayy/roll.git
git push -u origin master



print("Hello! Welcome to Hi-Roller!")
print("This is a free dice rolling simulation.")
print("Here is your number!Thanks for playing!")

from secrets import randbelow
print (randbelow(6))
 
while True:
    text = input ("Please type 'yes' to roll again for your number(or 'quit' to exit): ").lower()
    if text == "yes":
        print (randbelow(6))
        
    elif text == "quit":
        print("Thank you!Come again.")
        break
    else:
        print ("Please try again")
        
    
    