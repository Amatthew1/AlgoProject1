import time
def multiply(num1, num2):

    startStamp = time.time()
    #Convert the 1st number to binary
    num1Array = decToBin(num1)
    
    if num1 == 0 or num2 ==0:
        return 0
    if num1 == 1:
        return num2
    if num2 == 1:
        return num1
    
    #Add num1Array to itself num2 times
    summedArray = num1Array #base case of 1 is already taken care of
    product = 0
    
    for times in genrange(0,num2-1): 
        summedArray = addBinArray(summedArray, num1Array) #Take the sum so far and add num1 to it
        if times%1000 == 0:
            print str(times) + " of " + str(num2)
            print "total time taken" + str(startStamp-time.time())
    #Convert the array back to decimal
    product = binToDec(summedArray)
    #print "product: " + str(product) #
    
def multiplyQuick(num1, num2):
    startStamp = time.time()
    if num1 == 0 or num2 ==0:
        return 0
    if num1 == 1:
        return num2
    if num2 == 1:
        return num1
    sum = 0
    for times in genrange(0, num2-1):
        sum += num1
        if times%1000 == 0:
            print str(times) + " of " + str(num2)
            print "total time taken" + str(startStamp-time.time())

def decToBin(number):

    binArray = []
    while number > 0: #Repeat until we have converted the whole number
        a = number % 2
        binArray.append(a)
        number = (number-a)/2

    return binArray ##This is intentinally backwards

def binToDec(numArray):

    decNum = 0
    for index in range(len(numArray)):
        decNum += numArray[index]*(2**index)

    return decNum
    
def addBinArray(numArray, numArray2):
    
    #Force arrays to be the same size #######I bet this impacts runtime a wii bit
    #In this case array1 will always be equal to or bigger than array2
    for index in range(len(numArray)-len(numArray2)):
        numArray2.append(0)

    carry = 0
    summedArray = []
    for index in range(len(numArray)):
        #Add the values from both indexes and a carry, if applicable
        carry, digit = addBinary(numArray[index], numArray2[index], carry)
        summedArray.append(digit)
    summedArray.append(carry) #incase the last digit overloaded
    
    return summedArray ##This is still backwards 
    
def addBinary(num, num2, carryIn): #Each contain a value of 1, up to 3

    if num and num2 and carryIn: # ABC = 3 
        carryOut = 1
        digit = 1
    if num and num2 and not carryIn: # AB = 2
        carryOut = 1
        digit = 0
    if num and not num2 and carryIn: # AC = 2
        carryOut = 1
        digit = 0
    if not num and num2 and carryIn: # BC = 2
        carryOut = 1
        digit = 0
    if num and not num2 and not carryIn: # A = 1
        carryOut = 0
        digit = 1
    if not num and num2 and not carryIn: # B = 1
        carryOut = 0
        digit = 1
    if not num and not num2 and carryIn: # C = 1
        carryOut = 0
        digit = 1
    if not num and not num2 and not carryIn: 
        carryOut = 0
        digit = 0
    
    return carryOut, digit
    
def genrange(min,max,stride=1): #from Stack-overflow
    val=min
    while val<max:
        yield val
        val+=stride