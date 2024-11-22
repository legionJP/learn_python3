print('Imported my_module...')

test = 'Test String'

def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
'''
def find_index1(search , target):
    for i , value in enumerate(search):
        if value == target:
            return i
    return -1    
    '''