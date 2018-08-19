# Square Guessing Game :AAG

import random

score = 0
fscore = 0

print('''
                            Square Guessing Game :AAG
''')

x,y = map(int,input("Enter Range of Values as two space seperated numbers: ").split())
while fscore<5:
    ans=0
    s = random.randint(x,y)

    ans = input("Enter the square of "+str(s)+": ")
    if not ans.isdigit():
        print("Ener Numbers Only")
        continue
    ans = int(ans)
    if s*s == ans:
        print("Correct")
        score+=1
    else:
        
        fscore+=1
        print("Ans is:",s*s)

print("Your Score is: ",score," and Errors are:", fscore)            
