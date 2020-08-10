'''

Recursion

1.)  Function that calls itself

2.)  Breakcase

3.)  Forward progress(step)

'''

def my_func():
    if(True):
        my_func()

# my_func()




def print_num():
    for num in range(10):
        print num

# print_num()

def r_print_num(num):
    if num < 5:
        r_print_num(num + 1)
        print(num)

# r_print_num(0)

# 1.) r_print_num()
# 2.) 10 == num
# 3.) Forward progress num + 1 

def r_sigma(num, sum=0):
    print('sum', sum)
    print('num', num)
    if num > 0:
        sum += num
        r_sigma(num - 1, sum)
        print('-'*30)
    

    # num = 4
    # sum 0->4
    # 4 + 3 + 2 + 1
    # 10
r_sigma(4)

def r_factoral(num):
    print('num', num)
    if num < 2:
        return num
    x = num * r_factoral(num - 1)
    print('x', x)
    return x

r_factoral(4)