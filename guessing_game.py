#guess the number program
import random
initialGuess = random.randint(1,20)
print('what is your name?')
myName = input()
print(myName + ', lets play a guessing game')
print('I\'m thinking of a number between 1-20, can you guess what it is?')

for guesses in range(6):
    guessedNo = int(input())
    if guessedNo == initialGuess:
        print('wow, that\'s right?')
        break
    elif guessedNo > initialGuess:
        print('thats a little high')
    elif guessedNo < initialGuess:
        print('thats a little less')

print('sorry!, ur chances r over, the no. I guessed is ' + str(initialGuess))

