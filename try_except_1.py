#try and except ... catching one error at a time

def divideby(aNum):
    try:
        return 43 / aNum
    except:
        print('u r trying to divide by zero')
print(divideby(23))
print(divideby(3))
print(divideby(0))
print(divideby(13))
