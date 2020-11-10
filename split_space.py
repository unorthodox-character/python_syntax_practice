print('enter a sentence')
sentence = input()
wordList =sentence.split() # split returns strings in a data type "LIST"
#print(wordList)
for words in range(len(wordList)):
    if wordList[words] == 'ankit':
        print('aahaa!! ,  found you ankit')
    
