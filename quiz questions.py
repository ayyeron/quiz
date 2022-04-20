print("Welcome To My Super Duper Extremely Difficult Quiz hehe")

playing = input("Hey YOU do you dare to try this quiz? ")

if playing.lower() != "yes":
    quit()

print("Okay lets start the quiz! ")
score = 0 

answer = input("What does B.C stand for? ")
if answer.lower() == "british columbia":
    print('You indubitably got it correct! ')
    score += 1
else:
    print('bruh how do you get that wrong')

answer = input("Who is the prime minister? ")
if answer.lower() =="justin trudeau":
    print('You indubitably got it correct! ')
    score += 1
else:
    print('bruh how do you get that wrong')

answer = input("Who got slapped at the oscars awards in 2022? ")
if answer.lower() =="chris rock":
    print('you indubitably got it correct! ')
    score += 1
else:
    print('bruh how do you get that wrong')

answer = input("What did the Fox Say? hint: not actual fox noises ")
if answer.lower() =="ring-ding-ding-ding-dingeringeding":
    print('You indubitably got it correct! ')
    score += 1
else:
    print('bruh *mikewazowskibruhstare* ')

answer = int(input("What year did the toronto rapter win the championship? "))
if answer() =="2019":
    print('You indubitably got it correct! ')
    score += 1
else:
    print('bruh how do you get that wrong')

answer = input("What known wrestler is considered invisible to see? ")
if answer.lower() =="john cena":
    print('You indubitably got it correct! ')
    score += 1
else:
    print('bruh how do you get that wrong')

answer = input("Who is the rock? ")
if answer.lower() =="dwayane johnson":
    print('You indubitably got it correct! ')
    score += 1
else:
    print('bruh how do you get that wrong')

answer = int(input("How many months of the year have 28 days in them? "))
if answer() =="12":
    print('You indubitably got it correct! ')
    score += 1
else:
    print('bruh how do you get that wrong')

answer = int(input("How mamy mooons does Mars have? "))
if answer() =="2":
    print('You indubitably got it correct! ')
    score += 1
else:
    print('bruh how do you get that wrong')

answer = int(input("What year was i born? "))
if answer() =="2004":
    print('You indubitably got it correct! ')
    score += 1
else:
    print('bruh how do you get that wrong')

print("you got" + str(score) + "questions right" )
print("you got" + str((score / 4 * 100) + "%." ))