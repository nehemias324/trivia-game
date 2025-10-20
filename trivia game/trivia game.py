"""
Filename: trivia_game.py
Author: <Salvatierra, Nehemias>
Created: <9/11/2025>
Instructor: Holtslander
"""


score = 0
correct = 0

q1 = input("what is the capital of France?\n").lower()
if q1 == "paris":
    Score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 1
    print (score, correct)

q2 = input("what is the capital of Germany?\n").lower()
if q2 == "berlin":
     score = score + 4
     correct = correct + 2
else:
     if score > 0:
         score = score - 1
         correct = correct + 1
     print (score, correct)

q3 = input("what is the capital of Italy?\n").lower()
if q3 == "rome":
    score = score + 6
    correct = correct + 3
else:
     if score > 0:
         score = score - 1
         correct = correct + 1
     print (score, correct)

q4 = input("what is the capital of england?\n").lower()
if q4 == "london":
    Score = score + 8
    correct = correct + 4
else:
    if score > 0:
        score = score - 1
    print (score, correct)

q5 = input("what is the capital of the United states of America?\n").lower()
if q5 == "washington, D.C":
    Score = score + 10
    correct = correct + 5
else:
    if score > 0:
        score = score - 1
    print (score, correct)

q6 = input("what is the capital of india\n")
if q6 == "new delhi":
   Score = score + 12
   correct = correct + 6
else:
    if score > 0:
        score = score - 1
    print (score, correct)

q7 = input("what is the capital of spain?\n").lower()
if q7 == "madrid":
    Score = score + 14
    correct = correct + 7
else:
    if score > 0:
        score = score - 1
    print (score, correct)

q8 = input("what is the capital of australia?\n").lower()
if q8 == "Canberra":
    Score = score + 16
    correct = correct + 8
else:
    if score > 0:
        score = score - 1
    print (score, correct)

q9 = input("what is the capital of netherlands?\n").lower()
if q9 == "amsterdam":
    Score = score + 18
    correct = correct + 9
else:
     if score > 0:
         score = score - 1
     print (score, correct)

q10 = input("what is the capital of thailand?\n").lower()
if q10 == "bangkok":
    Score = score + 20
    correct = correct + 8
else:
    if score > 0:
        score = score - 1
    print (score, correct)