#input your word here
word = input('Enter word: ')
#this reverses the word
reverse_word = word[::-1]
#this gets the number of letters in the string
d = len(reverse_word)
#we run this for loop the same number of times the numbers are equal to
for i in range(d):
    #i'm using this list to convert the word into an array so we can pick them index by index
    a = list(reverse_word)
    #multiply each index by 3
    count = a[i] * 3
    #output the code
    print(count)