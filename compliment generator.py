import random
#Compliment Generator- 31/7/2025
print("Hey, welcome to Compliment!")
name = input("What's your name?: ")
compliments = [
  "Your name is beautiful.",
  "You're smarter than you think",
  "You're unstoppable",
  "You give of a warm energy",
  "You're so charismatic"
  ]

again = True
while True and again:
  compliment = random.choice(compliments)
  
  print(f"{name}, {compliment}")
  if compliment == compliments[0]:
    meaning = input("What does it mean?: ")
    print("Wow that's so meaningful!")
  restart = input("Should I give you another compliment?: ").lower()
  if restart == "yes":
    continue
  else:
    again = False
    break
