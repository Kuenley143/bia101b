
#searching
#sorting 

#problem 1
# ?input
user_input = [1,2,3,4,5,6,7,8,9,10]

# ?0 Check to see if a certain number exixt in the user input array
n = 14

# linear search 
result = False # !a variable to keep track of your answer

for e in user_input:
    if e == n: 
        result = True 

if result == True:
    print('Found')
else:
    print('Not found')
    
# if else, for loops, print, calculations(+, -)

#Time: O(n)
#input = [1,2,3,4,5]
#for i in input:
    #if i == 1: #O(9)
        #continue
    #print("hi")

input = [1,2,1,1,1,1]
# O(N^2)
for i in input: # n^3 + n^2
    break
    print('hi')
    for k in input: # n
        print('hello')
    for m in input: # n^2
        print('hello')
        for l in input: # n
            print('hello')

    for k in input:
        print('hello')

# n^2 + n = n^2