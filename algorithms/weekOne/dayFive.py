def zip_list(list_one, list_two):
    pass


zip_list_result = zip_list(['a','b','c'], [1,2,3])
print(zip_list_result)
#{ 'a': 1, 'b': 2, 'c': 3 }

def invert_hash(obj_input):
    key_list = obj_input.keys()
    for key in key_list:
        obj_input[obj_input[key]] = key
        del obj_input[key]
    
    return obj_input
    # pass

invert_hash_result = invert_hash({ 'a': 'z', 'b': 'y', 'c':'z' })
print(invert_hash_result)
# { 'x': 'a', 'y': 'b', 'z': 'c' }

# Bonus

def book_index(list_input):
    pass

book_index_result = book_index([1,4,5,6,12,16,17])
print(book_index_result)
# '1, 4-6, 12, 16-17'