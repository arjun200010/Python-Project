import random
def check(user,comp):
    if(comp ==user):
        return 0
    if(comp==0 and user==1):
        return -1
    if(comp==1 and user==2):
        return -1
comp=random.randint(0,2)
user=int(input("Choose snake 0, gun 1 and water 2 \n"))
score=check(user,comp)
if(score==0):
    print("Its draw")
elif(score==-1):
    print("You lose")
else:
    print("you wins")