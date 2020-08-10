def binary_search(list_input, val):
    pass








def r_binary_search(list_input, val, start=0, end=None):
    if end == None:
        end = len(list_input)-1


    r_binary_search(list_input, val, start, end)

r_binary_search([1,2,3,4,5,6,7,8,9], 4)