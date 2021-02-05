#Question 1

# User login application:
# 		-Get Username and Password values from the user
# 		-Check the values in an if statement and tell the user if they were successful.
#Extra:
# -Try Building the same user login application but this time, use a dictionary.

Username = 'JohnLegend'
Password = 'Iamlegend'
Input_user = input("Please Enter your username: ")
Input_pass = input("Please Enter password to proceed: ")
if (Username == Input_user) and (Password == Input_pass):
	print("Login is Successful")
else:
	print("Enter correct username and password")