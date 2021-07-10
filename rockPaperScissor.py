import random
computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
user_choice = input('Choose Rock, Paper or Scissors\n')
if computer_choice == user_choice:
    print ("Its a TIE! Try one more time. The computer choose" + " " + computer_choice)
elif computer_choice == 'Rock' and user_choice == 'Paper':
    print('User WINs, Computers choice was' + " " + computer_choice)
elif computer_choice == 'Paper' and  user_choice == 'Scissors':
    print('User WINs, Computers choice was' + " " + computer_choice)
elif computer_choice == 'Scissors' and user_choice == 'Rock':
    print ('You Win! The Comupters choice was' +  " " + computer_choice)
else:
    print('You loss, The computers choice was' + " " + computer_choice)

