temperature = int(input("What is the current Teperature?"))
if int(temperature > 50):
    print("It's too hot")
elif int(temperature > 90):
    print("Its Hot Hot!")
else int(temperature < 10):
    print("Its cold.")
    print("Stay Inside")