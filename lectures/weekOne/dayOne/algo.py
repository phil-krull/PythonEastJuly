'''
def removeBlanks(str_input):
    newStr = ""
    for i in range(len(str_input)):
        if not str_input[i] == ' ':
            newStr += str_input[i]
    return newStr

# result = removeBlanks('Today is Monday')
print(result)
'''

# String Interpolation - add variable to a string

my_num = 8
str_one = 'abd'
num_one = 1
num_two = 2
# str()
# int()

print(type(my_num))
print(type(str_one))

# 1. my_str = 'The num ' + str(my_num) +  ' is my number'
# 2. my_str = 'The num {a} is my number {b} {c}'.format(c=num_one, a=my_num, b=num_two)
my_str = f'The num {num_one} is my number {my_num} {num_two}'

print(my_str)