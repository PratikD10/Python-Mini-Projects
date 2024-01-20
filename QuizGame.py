print("Welcome to my Quiz")

playing = input("Are you Ready to Play? ")
if playing.lower() != "yes":
    quit()

print("Okay Great! Let's Play :)")
score=0


answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!!!")
    score+=1
else:
    print("Oh Sorry that's Incorrect :(")

answer = input("What goes GPU stand for? ")
if answer.lower() == "Graphics processing unit":
    print("Correct!!!")
    score+=1
else:
    print("Oh Sorry that's Incorrect :(")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!!!")
    score+=1
else:
    print("Oh Sorry that's Incorrect :(")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct!!!")
    score+=1
else:
    print("Oh Sorry that's Incorrect :(")


print("You final score is "+ str(score) +" !")
print("You final score is "+ str((score/4)*100) +"%ye")
if score>2:
    print("You Passed!")
else:
    print("You Failed :(")

