import string
inputTextFile = open("sample-file.txt")
wordFrequencyDictionary ={}


for line in inputTextFile:
    line = line.translate(str.maketrans('', '', string.punctuation)).lower()
    lineAsList = [word for word in line.split() if len(word) >= 2]
    for word in lineAsList:
        if word in wordFrequencyDictionary.keys():
            wordFrequencyDictionary[word] += 1  
        else:
            wordFrequencyDictionary[word] = 1
tenMostFrequentWords = sorted(wordFrequencyDictionary.items(),key= lambda word: word[1],reverse=True)[:10]

print(tenMostFrequentWords)