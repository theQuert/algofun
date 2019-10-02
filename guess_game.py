import math, random

real_ans = 9
i = j = 1
while i <= 3:
    guess = int(input('Guess :'))
    if guess != real_ans:
        j += 1
    else:
        why = True
        print(f"You've got the right number {real_ans} !!!")
        break
    i += 1
if j == 4:
    print('Sorry you failed ! ')