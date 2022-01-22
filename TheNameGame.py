import random
UrName = random.choice(['Rose', 'Lucky', 'Lily', 'Josh', 'Jose'])
ThatNam = input("Whats that guys name?\n")
if UrName == ThatNam:
    print("Thats the name! That guys name was" + " " + str(ThatNam))
else:
    print("Thats not the name! That guys name is" + " " + str(ThatNam))