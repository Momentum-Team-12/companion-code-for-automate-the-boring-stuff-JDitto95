#This program says hello and asks for my name.
print('Hello, World')
print('What is your name?')   #ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')   #ask for their age
myAge = input()
print('You will be' + str(int(myAge) + 1) + ' in a year.')



# Example of a "problem" in python.
# def sum(numbers):
#     numbers_copy = numbers.copy()
#     sum = 0 
#     while len(numbers_copy) > 0:
#         sum += numbers[len(numbers_copy) -1]
#         print('sum:', sum)
#         numbers_copy.pop()
#         print('numbers:', numbers_copy)
#     print(sum)
#     return(sum)
# my_sum = sum([1, 2, 3, 17])