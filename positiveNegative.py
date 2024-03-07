#objective: 
# crate a program that takesin user input
# and determines if the number takes is positive or negative or zero 
# print : "Your number is positive"or " Your number is negative"

# if else
# print()
# input()

# 3 mins

# Break down the problem 
# * 1. Take in user input
# * check the TYPE of the input 
# * if the type is string, how do you convert it an int?
# * 2. check if the number is positive or negative or zero
# ! a == b (is it equal to)
# ! a != b (Not equal to)
# ! a > b (is a greater than b)
# ! a < b (is a less than b)
# ! a >= b (is a greater than or equal to b)
# ! a <= b (is a less than or equal to b)
#* - you will be comparing numbers and not string
# ?3. Print the result



# 1. get user input 
userInput = input('Please type any number: ')
userInputType = type(userInput) 
print('The type of user input is:', userInputType)

userInputNumber = int(userInput)
print('The type of userInputNumber is:',type(userInputNumber))

if userInputNumber > 0:
    print('The number is positive')

elif userInputNumber < 0:
    print('The number is negative')

elif userInputNumber == 0:
    print('The number is zero')