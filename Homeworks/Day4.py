#Question
#Finding prime numbers between 0 and 100 using functions
def Is_Prime(x):
    '''
        Function to find whether a number is prime or not
        input: an integer
        output: bool value
    '''
    if x<=3: 
        return x > 1 #returns True if number is 2,3

    if x%2 == 0 or x%3 == 0: #if number is divisible by 2 or 3 return False
        return False 
    
    i = 5
    while i**2 <= x:         #all prime numbers greater than 3 are of form (6k+1)or(6k-1)
        if x%i == 0 or x%(i+2) == 0:
            return False
        i+=6
    return True

for i in range(0,101):
    if Is_Prime(i):
        print(i,end=' ')    #print the number if it is prime number