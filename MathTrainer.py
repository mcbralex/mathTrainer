#Alex Mcbride CIS345 12pm PE2

import os
import random

operators = ('+','-','*','/')
correct = list()
answer = 0
pointsEarned = 0
pointsTotal = 0
runApp = 'y'

while runApp == 'y':
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    sign = random.choice(operators)
    pointsTotal += 1

    if sign == '+':
        answer = number1+number2
    elif sign == '-':
        answer = number1-number2
    elif sign == '*':
        answer = number1*number2
    elif sign == '/':
        answer = round(number1/number2,3)

    os.system('clear')
    print("###Math Trainer###")
    studentAnswer = input(f"Problem {pointsTotal}: {number1} {sign} {number2} = ")
    if studentAnswer == str(answer):
        print("You are Correct!")
        correct.append(studentAnswer)
        pointsEarned += 1
        print(f"Points Earned: {pointsEarned} out of {pointsTotal}  Average: {(pointsEarned/pointsTotal)* 100}% ")
        runApp = input("Do you want another question? (y/n)? ").casefold()


print(f"you scored {(pointsEarned/pointsTotal)* 100}% and got the following right")
for element in correct:
    print(element)





