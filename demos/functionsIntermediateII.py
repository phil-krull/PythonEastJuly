# Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# print(type(students))
# print(students[0])
# print(type(students[0]))
# print(students[0]['last_name'])

# students[0]['last_name'] = 'Bryant'
# print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
# In the sports_directory, change 'Messi' to 'Andres'
# print(sports_directory['soccer'])
# print(sports_directory[1])
# if 1 in sports_directory:
#     print('1 is there')
# else:
#     print('its not')
# sports_directory['soccer'][0] = "Andres"


# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# print(x)
# print(type(x))
# print(x[0])
# print('>'*40)
# print(x[1][0])
# x[1][0] = 15
# print(type(x[1]))
# print('='*40)
# print(x)


z = [ {'x': 10, 'y': 20} ]
# Change the value 20 in z to 30
# print(z[0]['y'])
# z[0]['y'] = 30
# print(z)




# Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(student_list):
    for student in student_list:
        student_builder = ''
        isFirst = True
        for x,y in student.items():
            student_builder += x
            student_builder += ' - '
            student_builder += y
            if isFirst is True:
                student_builder += ', '
            isFirst = False
            # print(f'{x} {y}')
        print('-'*40)
        print(student_builder)
        # print(student['first_name'])
        # print(student['last_name'])

# iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel



# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, 

def iterateDictionary2(key_name, some_list):
    print(key_name)
    print(type(key_name))
    for item in some_list:
        print(item[key_name])

# iterateDictionary2('first_name', students) 

# should output:

# Michael
# John
# Mark
# KB
# And 
# print('^'*40)
# iterateDictionary2('last_name', students)

# Jordan
# Rosales
# Guillen
# Tonel



# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, val in some_dict.items():
        # print('key', key)
        # print('val', val)
        print(f'{len(val)} {key.upper()}')
        for list_item in val:
            print(list_item)
printInfo(dojo)
print(dojo)

# # output:

# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon