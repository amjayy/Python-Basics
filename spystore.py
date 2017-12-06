
print("Welcome to B3 Central!")
print("Hi, what's your name?")
name=input()
print("Excellent! Hi, " +name)
print("What state do you live in?")
state=input()
print("Fantastic!")
print(name+ ", I see others in your area like this product,would you like to browse them?")
answer=input()
if answer =="yes":
    print("Wonderful! Click the link below")
    
if answer =="no":
    print ("No worries! What would you like to view first?")
    array = ["shoes", "accessories","home","clothing"]
    answer=input().lower()
else:
    print("Invalid Response") 
if answer =="home":
    print("Would you like to see the indoor or outdoor collection?")
    answer=input().lower()
if answer =="indoor":
    array2=["bedroom", "kitchen", "kid's room","bathroom", "dining room"]
    answer=input().lower()

    
if answer =="accessories":
    print("Friendly notice:The return policy of jewelry is 30 days.")
    answer=input().lower
    array4= ["necklaces", "earrings", "bracelets", "rings"]
    








