def yourName():
    global spam
    
    print(spam)
def myName():
    spam =50
    yourName()
    #print(spam)
spam = 23
myName()
