print("Welcome to my computer qiiz!")

playing =input(" Do want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay| Let's play :)")
score =0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorerect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorerect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorerect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("correct!")
    score += 1
else:
    print("incorerect!")

print("You got "+ str(score)  + " question correct")
print("You got "+ str((score/4)*100) + " %.")

