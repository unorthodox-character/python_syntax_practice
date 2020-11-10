print('what\'s ur name?')
myName = input()
print('its good to meet you, ' + myName )

while True:
    print('so, how many dogs do you have?')
    try:
        noOfCats = int(input())
        if noOfCats >= 3 and noOfCats <500:
            print('that\'s a lot of dogs')
            break
        elif noOfCats <3 and noOfCats >=0:
            print('thats not a lot')
            break
        elif noOfCats <0 or noOfCats >500:
            print('r u crazy?, lets do this again')
    except ValueError:
        print('you did not type an integer value, lets try that again')
