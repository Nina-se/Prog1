import random

print("10 Easy counting for kids")
print("<<<<<<<<<<<>>>>>>>>>>>>>>")
for number in range(10):
    fnum = random.randint(1, 100)
    snum = random.randint(1, 100)
    while True:
        task = str(fnum)+" + "+ str(snum)+" = "
        answer = int(input(task))
        if answer == (fnum + snum):
            print("Excellent!")
            break
        else:
            print("Almost there, try more!")
print("Game is completed. See you next day!")
