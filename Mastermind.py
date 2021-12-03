import random

class Computer:
    #This is the computer opponent that creates code
    def __init__(self):
        self.colors = "BWRYGb"
    def chooseDif(self, level):
        if level == 5:
            return 6
        elif level == 4:
            return 6
        elif level == 3:
            return 8
        elif level == 2:
            return 10
        else:
            return 12
    def code(self, level):
        listCode = list("EEEE")
        n = 0
        if level == 5:
            for part in listCode:
                num = random.randint(0,6)
                if num == 6:
                    pass
                else:
                    listCode[n] = self.colors[num]
                n += 1
            theCode = "".join(listCode)
            return theCode
        else:
            for part in listCode:
                num = random.randint(0,5)
                listCode[n] = self.colors[num]
                n += 1
            theCode = "".join(listCode)
            return theCode
    def feedback(self, sequence, playerGuess):
        if sequence == playerGuess:
            return 1
        else:
            #implement comparison between sequence and playerGuess
            y = 0
            simCount = 0
            sameCount = 0
            checkNums = []
            #same = [i for i, j in zip(sequence, playerGuess) if i == j]
            for part in playerGuess:
                #print(part)
                #print(playerGuess)
                if part == sequence[y]:
                    sameCount += 1
                    checkNums += [part]
                    playerGuess = playerGuess[1:]
                elif playerGuess.count(part) > 1:
                    playerGuess = playerGuess[1:]
                elif part in sequence:
                    if part not in checkNums:
                        simCount += 1
                    playerGuess = playerGuess[1:]
                else:
                    playerGuess = playerGuess[1:]
                y += 1
            return "You guessed", sameCount, "in the correct position and color. You also guessed", simCount, "that had the correct color but wrong position."


def playMastermind():
    print("Welcome to Mastermind, Python Edition! Can you crack the code created by this computer code? This program will generate a random list of four colors. Your job is to guess the correct color and position of all four components of the list. You can decide to do this at differing levels of difficulty. The harder levels provide a smaller number of guesses to get the code right, and the hardest level even allows empty spaces (E) rather than a color. Once a guess is given as a string containing four letters (colors), the computer will compare the guess to the actual code and provide feedback. This will say if one of the four is correct in both position AND color and/or if it is the correct color but in the wrong position. However, it will not tell you which parts of your guess triggered the feedback. With the provided feedback after each guess, your job is to crack the code before the guess limit.")
    escape = 0
    comp = Computer()
    while escape != 1:
        count = 0
        dif = int(input("What difficulty from Beginner (1) to Expert (5) would you like to play at?"))
        print("For reference, here are the colors you can choose from (represented by the first letter of a color):", comp.colors)    
        print("Alright! Let's begin!")
        code = comp.code(dif)
        numRounds = comp.chooseDif(dif)
        while count < numRounds:
            print("Guesses remaining:", numRounds - count)
            guess = input("Please enter a guess!")
            check = comp.feedback(code, guess)
            if check == 1:
                count = 100
                print("Congrats! You have beaten the Mastermind!")
            elif count+1 == numRounds:
                print("You lost! The sequence was", code)
            else:
                print(check)
            count += 1
        escape = int(input("Enter 1 if you would like to stop, otherwise enter 0 to start a new game!"))
            
            
playMastermind()

                
        
