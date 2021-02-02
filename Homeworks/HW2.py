#Explain your work

#Question 1
#2. Ask the user to input a single digit integer to a variable 'n'. 
# Then print out all of the even numbers from 0 to n (including n).

n = int(input("Please enter a integer between 0 to 9: ")) #recieving input from the user
even_numbers = [i for i in range(1,n+1) if i%2 == 0] #list containing even numbers
print(even_numbers)