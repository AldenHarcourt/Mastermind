import copy
import random
'''
Master Mind Game
'''
class computerGuessing:

    def __init__(self):
        '''
        Constructs all possible keys [1, 1, 1, 1] through [6, 6, 6, 6]
        Data: the list of possible keys
        '''        
        self.possibleKeys = []
        for i in range(1, 7, 1):
            for j in range(1, 7, 1):
                for k in range(1, 7, 1):
                    for w in range(1, 7, 1):
                        self.possibleKeys.append([i, j, k, w])
    
    def getPossibleKeys(self):
        '''returns the current list of possible keys'''
        return self.possibleKeys
    
    def setPossibleKeys(self, newPossibleKeys):
        '''
        sets the list of new possible keys to a deepcopy of the input
        takes in list of new Possible Keys
        '''
        self.possibleKeys = copy.deepcopy(newPossibleKeys)
    
    def removePossibleKey(self, keyToRemove):
        '''
        takes in key that should be removed
        finds the index of the key you want to remove and then pops it out
        '''
        x = self.possibleKeys.index(keyToRemove)
        self.possibleKeys.pop(x)

    def getKeyFromIndex(self, index):
        '''
        takes in an index
        return the key in that index
        '''
        return self.getPossibleKeys()[index]

    def doRMatch(self, R, key, guess):
        '''
        takes in a possible key and a possible guess
        checks if the number of red pins matches the number that should be reurned with the key and guess
        returns whether the check is true or false
        '''
        return (R == self.redPins(key, guess))
    
    def doWMatch(self, W, key, guess):
        '''
        takes in a possible key and a possible guess
        checks if the number of white pins matches the number that should be reurned with the key and guess
        returns whether the check is true or false
        '''
        key2 = copy.deepcopy(key)
        guess2 = copy.deepcopy(guess)
        return (W == self.whitePins(key2, guess2))

    def editPossibleKeys(self, indexOfKeysWeWant):
        '''
        takes the indexes of keys we want to keep
        removes the other keys from the list of possible keys
        indexOfKeysWeWant: the indexes of the current valid keys given red and white pins
        calls getPossibleKeys
        calls setPossibleKeys
        '''
        newList = []
        for g in range(len(indexOfKeysWeWant)):
            newList.append(self.getPossibleKeys()[indexOfKeysWeWant[g]])
        self.setPossibleKeys(newList)

    def removePossibleKeysDueToRW(self, numberR, numberW, guess):
        '''
        takes in number of red pins, number of white pins, and the key guessed by the computer
        checks to see which keys are still valid given the red and white pins
        Parameters
        numberR: number of red pins
        numberW: number of white pins
        guess: key last guessed by the computer
        calls getPossibleKeys
        calls doRMatch
        calls doWMatch
        cals getKeyFrom Index
        calls editPossibleKeys
        '''
        weWillBeKeeping = []
        poss = self.getPossibleKeys()
        for i in range(len(poss)):
            if (self.doRMatch(numberR, self.getKeyFromIndex(i), guess) and  self.doWMatch(numberW, self.getKeyFromIndex(i), guess)):
                weWillBeKeeping.append(i)
        self.editPossibleKeys(weWillBeKeeping)

    def redPins(self, key, guess):
        '''
        returns the location of the red pins
        guess: The guess the computer makes
        calls:
        self.key
        '''
        totalRedPinsSoFar = 0
        for i in range(len(key)):
            if key[i] == guess[i]:
                totalRedPinsSoFar += 1
        return totalRedPinsSoFar

    def redPinsLocations(self, key, guess):
        '''
        returns the location of the red pins
        guess: The guess the computer makes
        key: A possible key for the computer to guess
        calls:
        self.key
        '''
        locations = []
        for i in range(len(key)):
            if key[i] == guess[i]:
                locations.append(i)
        return locations

    def whitePins(self, key, guess):
        '''
        returns the number of white pins based on
        a guess and a given key
        key: A possible key for the computer to guess
        guess: The guess the computer makes
        calls: redPinsLocations
        '''
        totalWhitePinsSoFar = 0
        tempKey = []
        for k in range(len(key)):
            tempKey.append(key[k])
        locationOfRedPins = self.redPinsLocations(key, guess)
        for i in range(len(locationOfRedPins)):
            tempKey[locationOfRedPins[i]] = -1
            guess[locationOfRedPins[i]] = -1
        for j in range(len(tempKey)):
            if tempKey[j] == -1:
                pass
            else:
                if(tempKey[j] in guess):
                    totalWhitePinsSoFar += 1
                    guess[guess.index(tempKey[j])] = -1
                    tempKey[j] = -1
        return totalWhitePinsSoFar
    
    def bestGuessDueTominMax(self):
        '''
        calculates the best possible guess for the computer to make
        and returns the best possible guess
        calls: getPossibleKeys, removePossibleKeysDueToRW, setPossibleKeys
        '''

        if len(self.getPossibleKeys()) == 1296:
            return [1, 1, 2, 2]
        currentSet = copy.deepcopy(self.getPossibleKeys())
        listOfGuessesLeft = []
        for i in range(len(self.getPossibleKeys())):
            worst = 0
            for r in range(0, 5):
                for w in range(0, 5):
                    self.removePossibleKeysDueToRW(r, w, self.getPossibleKeys()[i])
                    length = len(self.getPossibleKeys())
                    if (length > worst):
                        worst = length
                    self.setPossibleKeys(currentSet)
            listOfGuessesLeft.append(worst)
            
        return currentSet[listOfGuessesLeft.index(min(listOfGuessesLeft))]

class HumanGuessingMasterMind:
    def __init__(self):
       '''
        creates a random key of format [1, 2, 5, 6]
        uses random
        Data: the key in form [1, 2, 5, 6]
        '''
       self.key = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

    def getKey(self):
        '''
        return the key
        '''
        return self.key
    
    def redPins(self, guess):
        '''
        returns the number of the red pins
        guess: The guess the user makes
        calls:
        self.key
        '''
        totalRedPinsSoFar = 0
        for i in range(len(self.key)):
            if self.key[i] == guess[i]:
                totalRedPinsSoFar += 1
        return totalRedPinsSoFar

    def redPinsLocations(self, guess):
        '''
        returns the location of the red pins
        guess: The guess the user makes
        calls:
        self.key
        '''
        locations = []
        for i in range(len(self.key)):
            if self.key[i] == guess[i]:
                locations.append(i)
        return locations

    def whitePins(self, guess):
        '''
        Returns the number of white pins based on a guess
        guess: The guess that the human makes
        calls:
        redPinLocations()
        self.key
        '''
        totalWhitePinsSoFar = 0
        tempKey = []
        for k in range(len(self.key)):
            tempKey.append(self.key[k])
        locationOfRedPins = self.redPinsLocations(guess)
        for i in range(len(locationOfRedPins)):
            tempKey[locationOfRedPins[i]] = -1
            guess[locationOfRedPins[i]] = -1
        for j in range(len(tempKey)):
            if tempKey[j] == -1:
                pass
            else:
                if(tempKey[j] in guess):
                    totalWhitePinsSoFar += 1
                    guess[guess.index(tempKey[j])] = -1
                    tempKey[j] = -1
        return totalWhitePinsSoFar

def playHumanGuessing():
    '''
    The very fist thing this code does is ask how many guesses you want
    Then it loops through the number of guesses, taking a guess from the user every round
    After the guess the computer compares the guess to the key and prints out the number or red and white pins
    The cycle then repeats until eventuially the computer or human wins
    At this point the user is prompted to play again or not
    main() is called if the player wishes to play again, the program terminates if not
    Calls:
    HumanGuessingMasterMind()
    redPins()
    whitePins()
    getKey()
    main()
    '''
    howManyRounds = int(input('How many guesses do you want (9 is standard): '))
    print('Guess should be in the format: 1111')
    masterMind = HumanGuessingMasterMind()
    #print(masterMind.getKey())
    alreadyDone = False
    for i in range(howManyRounds):
        if(not alreadyDone):
            guessInput = int(input('Your guess is:'))
            guess = [int(w) for w in str(guessInput)]
            if(masterMind.redPins(guess) != 4):
                print('RedPins: ', masterMind.redPins(guess))
                print('WhitePins: ', masterMind.whitePins(guess))
            else:
                print('You won, the key was', masterMind.getKey(), 'and you guessed it in', i+1, 'tries')
                print('Congratulations')
                playAgain = input('Would you like to play again? ')
                if(playAgain == 'yes'):
                    main()
                else:
                    alreadyDone = True
                    pass
    if(alreadyDone):
        pass
    else:
        print('You ran out of tries')
        playAgain = input('Would you like to play again (yes or no)? ')
        if(playAgain == 'yes'):
            main()
        else:
            pass

def playComputerGuessing():
    '''
    The very fist thing this code does is ask how many guesses the computer should get
    Then it loops through the number of guesses, and guesses the bestGuessDueTominMax()
    After guessing the computer asks the user for th enumber of red pins and white pins
    These numbers are then put into removePossibleKeysDueToRW()
    The cycle then repeats until eventuially the computer or human wins
    At this point the user is prompted to play again or not
    main() is called if the player wishes to play again, the program terminates if not
    Calls:
    computerGuessing()
    removePOssibleKeysDueToRW()
    bestGuessDueTominMax()
    main()
    '''
    howManyRounds = int(input('How many guesses should I get (9 is standard): '))
    masterMind = computerGuessing()
    alreadyDone = False
    for i in range(howManyRounds):
        if(not alreadyDone):
            guess = masterMind.bestGuessDueTominMax()
            print('My guess is: ', guess)
            r = int(input('Red Pins:'))
            w = int(input('White Pins:'))
            if(r != 4):
                masterMind.removePossibleKeysDueToRW(r, w, guess)
            else:
                print('I won, the key was', guess, 'and I guessed it in', i+1, 'tries')
                print('Yayyy, Im so smart!')
                playAgain = input('Would you like to play again (yes or no)? ')
                if(playAgain == 'yes'):
                    main()
                else:
                    alreadyDone = True
                    pass
    if(alreadyDone):
        pass
    else:
        print('I ran out of guesses')
        playAgain = input('Would you like to play again (yes or no)? ')
        if(playAgain == 'yes'):
            main()
        else:
            pass

def main():
    '''
    Takes an input from user of whether the user would like to either have the key or guess
    Based on this input the computer will either call playHumanGuessing() or playComputerGuessing()
    '''
    inpu = input('Would you like to guess or have the key (guess or key or quit): ')
    if inpu == 'guess':
        playHumanGuessing()
    elif inpu == 'key':
        playComputerGuessing()
    elif inpu == 'quit':
        pass
    else:
        print('I think you had a typo')
        main()

main()