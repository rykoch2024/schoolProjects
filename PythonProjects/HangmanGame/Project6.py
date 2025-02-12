#Ryan Koch

import os.path
import random


#Create a dictionary for existing word list. 
# Adds each word to lists of same length words after removing "\n"
# if list does not exist, creates key:list pair 
def makeDictionary(file):
    global longestWord
    longestWord = 0
    thisFile = open(file, "r")
    newLine = thisFile.readline()
    retDict = {}

    while newLine:
        currWord = newLine
        currWord = currWord.replace("\n", "")
        key = len(currWord)
        if key in retDict:
            retDict[key].append(currWord)
        else:
            retDict.update({key: [currWord]})
            if key > longestWord:
                longestWord = key
        newLine = thisFile.readline()
    thisFile.close()
    return retDict


#Greeting and difficulty selection
def gameStart():
    print("Welcome to Hangman!")
    invalid  = True
    while invalid:
        wordLength = input("please select word length (3 to " + str(longestWord) + "):")
        print("You have chosen: " + str(wordLength))
        if int(wordLength) >= 3 and int(wordLength) <= longestWord:
            return int(wordLength)
        else:
            print("Invalid entry")


#Select word and remove from available list
def wordSelection(dictionary, key):
    word = random.choice(dictionary[key])
    dictionary[key].remove(word)
    return word


#Main build of the game, Hides the word from player views, handles guesses, handles game over conditions
def round(word):
    remainGuess = 2 * len(word) - 1
    guessedLetters = []
    victory = False
    visibleWord = ""

    #initialize the hidden word
    for i in range(len(word)):
        visibleWord = visibleWord + "*"

    #The actual game. Handling single letter guesses, multiple letter guesses, and invalid entries
    while remainGuess > 0:
        letterCount = 0
        print("word: " + visibleWord)
        print("Remaining guesses: " + str(remainGuess))
        playerGuess = input("Select a letter or guess the word: ")

        if len(playerGuess) > 1:

            if playerGuess == word:
                victory = True
                remainGuess = 0
            else:
                print("Incorrect")

        elif len(playerGuess) == 1 and playerGuess in guessedLetters:
            print("You have already guessed " + playerGuess + "!")
            remainGuess +=1
        elif len(playerGuess) == 1 and playerGuess.isalpha():
            i = 0
            guessedLetters.append(playerGuess)

            while i < len(word):
                if word[i].lower() == playerGuess.lower():
                    visibleWord = visibleWord[:i] + word[i] + visibleWord[i+1:]
                    letterCount += 1
                i += 1

            if letterCount == 1:
                print("Correct! There is 1 " + playerGuess + "!")
            elif letterCount > 1:
                print("Correct! There are " + str(letterCount) + " " + playerGuess + "'s!")
            else:
                print("incorrect")

            if word == visibleWord:
                victory = True
                remainGuess = 1

        else:
            print("Invalid Entry")
            remainGuess +=1

        remainGuess -= 1

    if victory:
        print("You Win! The word was " + word)
    else: 
        print("Out of guesses. Word was: " + word)

    

####
#Main Program
####

operatingFile = "wordlist.txt"

if os.path.exists(operatingFile):
    continueGame = True
    wordDict = makeDictionary(operatingFile)
    
    while continueGame:
        wordLength = gameStart()
        selectedWord = wordSelection(wordDict, wordLength)
        round(selectedWord)
        again  = input("Play again?(y/n): ")
        if again.lower() != "y":
            continueGame = False
else:
    print("File not found")

