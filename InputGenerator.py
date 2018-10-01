#Generate new inputs seperatly from the runtime of the main program
#4, 8, 16, 32, 64,128,512
import random
def generateNewInputs(lengthOfInput, numberOfInputs):

    #Create a unique file for each size of inputs so that extra time is not spent parsing excessive file
    fileName = str(lengthOfInput) + ".txt"
    f = open(fileName, 'w')
    ##Find the largest number of this size i.e. 4 would be 9999
    sizeString = ''
    for digit in range(lengthOfInput):
        
        sizeString += '9'

    maxSize= int(sizeString)

    for number in range(numberOfInputs + 1): #make one more, so each number can be used as an argument to the next
        randomInt = random.randint(0,maxSize)
        f.write(str(randomInt) + "\n")
    
    f.close()
    return fileName

