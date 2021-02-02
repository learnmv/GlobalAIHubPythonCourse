#Explain your work

#Question 1
#1. Create a list and swap the second half of the list with the first half the list and print this list on the screen

my_list = [1,2,3,4,5,6]

mid = len(my_list) // 2

first_half = my_list[0:mid] #first half of the list

second_half = my_list[mid:] #second half of the list

swapped_list = second_half + first_half #swapped list

print(swapped_list) #printing the list on the screen