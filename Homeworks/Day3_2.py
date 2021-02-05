#Question 1

# User login application:
# 		-Get Username and Password values from the user
# 		-Check the values in an if statement and tell the user if they were successful.
#Extra:
# -Try Building the same user login application but this time, use a dictionary.

user_dict = {'Username':'JohnLegend','Password':'Iamlegend'}
input_dict = {'Username':input('Please enter your username: '),'Password':input('Plese enter your password to proceed: ')}
if (user_dict['Username']==input_dict['Username']) and (user_dict['Password'] == input_dict['Password']):
    print("Login Successful !!!")
else:
    print("Please enter correct Username and Password")