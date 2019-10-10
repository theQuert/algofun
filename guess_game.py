import math, random

real_ans = 9
i = j = 1
for i in range(1, 4):
    guess = int(input('Guess :'))
    if guess != real_ans:
        j += 1
    else:
        why = True
        print(f"You've got the right number {real_ans} !!!")
        break

if j == 4:
    print('Sorry you failed ! ')