import random

user_wins=0
comp_wins=0
draws=0

options= ["rock", "paper", "scissors" ]

#options[0]="rock"
#options[1]="paper"
#options[2]=""


while True:
    user_input= input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input=="q":
        break


    if user_input not in options:
        continue

    
    random_number= random.randint(0,2)
    #rock:0, paper:1, scissors:2
    computer_pick = options[random_number]

    print('Computer Picked',computer_pick + ".")


    if user_input=='rock' and computer_pick=='scissors':
        print("You Won!")
        user_wins+=1
        
   
    elif user_input=='scissors' and computer_pick=='paper':
        print("You Won!")
        user_wins+=1
        

    elif user_input=='paper' and computer_pick=='rock':
        print("You Won!")
        user_wins+=1
        


    elif user_input==computer_pick:
        print("You Drew")
        draws+=1

    else:

        print("Computer Wins")
        comp_wins+=1

    



print("You've won ",user_wins,'times.')
print("Computer won",comp_wins,"times.")
print("You Drew",draws,'times.')
print("Goodbye!")

    