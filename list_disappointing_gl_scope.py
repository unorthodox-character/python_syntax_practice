# local and global scope with list to a function

def somfunc(list_para):
    rtnd = list_para.append("Ankit")
    return rtnd
spam = [1,2,3, 'iron', 'claude', 'rod']
print(somfunc(spam))

    
