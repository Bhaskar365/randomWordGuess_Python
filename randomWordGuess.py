import random

words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

random_word = random.choice(words)

inp = print('''
    -----------------------------------------------------
    -----------------------------------------------------                
    Welcome to random word guess. Type any word from a to z
    of the English letter system. Go ahead , take a guess.
    -----------------------------------------------------
    -----------------------------------------------------
    ''')


def check():
    count = int(input("Guess how many tries you want to guess the answer. : "))
    while (count != 0):
        guess = input('Guess the word : ')
        if guess == '':
            print('Enter a valid character')
        elif guess == random_word:
            print("correct")
        elif (guess > random_word):
            print('Entered word is to the right of correct word')
            count = count-1
        else:
            print('Entered word is to the left of correct word')
            count = count-1
        print(count, "tries left")
    if (count == 0):
        print("You run out of tries. You lose")


check()
