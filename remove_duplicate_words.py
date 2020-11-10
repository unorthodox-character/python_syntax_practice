import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
documentA = 'the man went out for a walk'
documentB = 'the children sat around the fire'
bagOfWordsA = documentA.split(' ')
bagOfWordsB = documentB.split(' ')
uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))#duita sentence baata one set of unique words haru chaaneko
numOfWordsA = dict.fromkeys(uniqueWords, 0)

for word in bagOfWordsA:
    numOfWordsA[word] += 1
numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1
def computeTF(wordDict, bagofWords):
    tfDict = {}
    bagOfWordsCount = len(bagofWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict
tfA = computeTF(numOfWordsA, bagOfWordsA)
tfB = computeTF(numOfWordsB, bagOfWordsB)
def computeIDF(documents):
    import math
    N = len(documents)
    idfDict = dict.fromkeys(documents[1].keys(), 0)
    print(idfDict)
    for document in documents:
        for word, val in document.items():
            if val == 0:
                print(idfDict[val])
            #print(idfDict[val])    
    #return idfDict
computeIDF([numOfWordsA, numOfWordsB])




