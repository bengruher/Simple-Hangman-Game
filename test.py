"""
@file hangman.py
@author Ben Gruher
@date June 22nd, 2019
"""

import random
CONST_NUM_WORDS = 57127
CONST_MAX_NUM_WRONG = 6 # matches max number of body parts on stick figure guy

def processGuess(letter, word, wordGuesses):
    correctGuess = False
    for i in range(len(word)):
        if letter == word[i]:
            wordGuesses[i] = True
            correctGuess = True
    return correctGuess

def printWord(word, wordGuesses):
    print("Here is your word: ")
    for i in range(len(word)):
        if wordGuesses[i] == True:
            print(word[i], end = '')
        else:
            print("-", end = '')
    print()

def printTree(numWrong):    
    zeroTree = "\n\t________" + "\n\t|      |" + "\n\t|" + "\n\t|" + "\n\t|" + "\n\t|" + "\n________|________\n"
    oneTree = "\n\t________" + "\n\t|      |" + "\n\t|      O" + "\n\t|" + "\n\t|" + "\n\t|" + "\n________|________\n"
    twoTree = "\n\t________" + "\n\t|      |" + "\n\t|      O" + "\n\t|      |" + "\n\t|" + "\n\t|" + "\n________|________\n"
    threeTree = "\n\t________" + "\n\t|      |" + "\n\t|      O" + "\n\t|   ---|" + "\n\t|" + "\n\t|" + "\n________|________\n"
    fourTree = "\n\t________" + "\n\t|      |" + "\n\t|      O" + "\n\t|   ---|---" + "\n\t|" + "\n\t|" + "\n________|________\n"
    fiveTree = "\n\t________" + "\n\t|      |" + "\n\t|      O" + "\n\t|   ---|---" + "\n\t|     /" + "\n\t|    /" + "\n________|________\n"
    sixTree = "\n\t________" + "\n\t|      |" + "\n\t|      O" + "\n\t|   ---|---" + "\n\t|     / \\" + "\n\t|    /   \\" + "\n________|________\n"

    switcher = {
        0: zeroTree,
        1: oneTree,
        2: twoTree,
        3: threeTree,
        4: fourTree,
        5: fiveTree,
        6: sixTree,
    }
    print(switcher.get(numWrong, "Could not generate tree"))

def testIfWon(wordGuesses):
    won = True
    for i in range(len(wordGuesses)):
        if wordGuesses[i] == False:
            won = False
    return won

def playGame():
    file = open("words.txt", "r")
    gameWon = False
    numWrongGuesses = 0

    # pick random word
    lineNum = random.randint(1, CONST_NUM_WORDS)
    for x in range(lineNum):
        file.readline()
    word = file.readline().strip("\n")

    # make bool 'array' and set to all False to start
    wordGuesses = []
    for i in range(len(word)):
        wordGuesses.append(False)

    printWord(word, wordGuesses)
    printTree(numWrongGuesses)

    pastGuesses = [] # keeps track of all the letters user has guessed

    while(not gameWon and numWrongGuesses < CONST_MAX_NUM_WRONG):
        if pastGuesses:
            print("Past Incorrect Guesses: ", end = '')
            for i in range(len(pastGuesses)):
                print(pastGuesses[i] + ", ", end = '')
            print()

        userGuess = input("Enter guess: ").upper()
        if len(userGuess) > 1 or not userGuess.isalpha():
            print("Invalid Input, Please Enter One Letter")
        elif userGuess not in pastGuesses:
            correctGuess = processGuess(userGuess, word, wordGuesses)
            if correctGuess:
                print("Correct Guess!\n")
            else:
                print("Incorrect Guess\n")
                numWrongGuesses += 1
                pastGuesses.append(userGuess)
            printTree(numWrongGuesses)
            print()
            printWord(word, wordGuesses)
            gameWon = testIfWon(wordGuesses)
        else:
            print("Letter already guessed. Guess new letter")
            printWord(word, wordGuesses)

    if gameWon:
        print("CONGRATULATIONS! YOU WON!")
    else:
        print("Sorry - you lost :(")

    file.close()

def main():
    print("Welcome to hangman!")
    name = input("Enter your name: ")
    print("Hello " + name + "! Here is your word: ")
    playAgain = True
    while playAgain:
        playGame()
        validInput = False
        while not validInput:
            repeat = input("Play again? [y/n]")
            if repeat != 'y' and repeat != 'n':
                print("Invalid Input")
            else:
                validInput = True
            if repeat == 'n':
                playAgain = False
    

if __name__ == '__main__':
    main()