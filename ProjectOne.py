from InputGenerator import generateNewInputs
from Multiplcation import multiply, multiplyQuick
from memory_profiler import profile
import time
import sys

outputFile = open('multiplier'  +str(time.time()) + ".txt","a+")

       
def main():
    assert len(sys.argv) ==3, 'Need size of inputs and number of inputs'
    size = int(sys.argv[1])
    numInputs = int(sys.argv[2])
    file = generateNewInputs(size, numInputs)
    
    #Setup outputFlow
    
    outputFile.write("Multiplier ran\n Size of inputs: " + str(size) + "\n Number of inputs: "+ str(numInputs) + "\n")

    numberArray = loadNumbers(file)
    executeMultiply(numberArray)
    
#Function that takes a file full of inputs, multiplies each line by the next
@profile(stream=outputFile)
def executeMultiply(numberArray):

    startStamp = time.time()
    for index in range(len(numberArray)-1): #skip the last input
        multiplyQuick(int(numberArray[index]),numberArray[index+1])
    totalRuntime = time.time() - startStamp 
    
    outputFile.write("Total run time: "+ str(totalRuntime) + "\n")

#Load the numbers from the file to keep that opertation sepeart from the runtime
def loadNumbers(file):

    with open(file) as ins:
        numberArray = []
        for line in ins:
           numberArray.append(int(line))
    return numberArray
    
if __name__ == '__main__':
    main()