def add_ten(param):
    return param + 10

def add_one(param):
    return param +1

num = float(input('What is number?'))
print('that plus 10 is : {}'.format(add_ten(num)))
print('and plus 1 is : {}'.format(add_one(num)))