#Explain your work

#Question 1
#1. Create a list and swap the second half of the list with the first half the list and print this list on the screen
#2. Ask the user to input a single digit integer to a variable 'n'. Then print out all of the even numbers from 0 to n.
my_list = [1,2,3,4,5,6]
mid = len(my_list) // 2
#first half of the list
first_half = my_list[0:mid]
#second half of the list
second_half = my_list[mid:]
#swapped list
swapped_list = second_half + first_half
print(swapped_list) #printing the list on the screen