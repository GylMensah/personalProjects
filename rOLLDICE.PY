import random
computerguess = random.randint(1,10)
userguess = input("guess a number between 1-10?")
if computerguess == userguess:
    print("yayyyyyyy")
else:
    print("try again")
