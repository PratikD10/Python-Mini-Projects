import random

top_of_range= input("Type a Number: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range <= 0:
        print("Pls type a no larger than 0")
        quit()
else:
    print("Pls type a Number next time")
    quit()

random_number = random.randint(0, top_of_range)
guesses=0

while True:
    guesses+=1
    user_guess= input("Make a guess: ")
    if user_guess.isdigit():
       user_guess=int(user_guess)

        
    else:
        print("Pls type a Number next time")
        continue


    if user_guess==random_number:
        print("You Got It!")
        break
    elif user_guess>top_of_range:
        print("Your guess is not in the Range")

    elif user_guess>random_number:
            print("You were above the No!")
    else:
            print("You were below the Number!")
        
print("You got it in",guesses,"guesses")
