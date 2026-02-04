import string
inputTextFile = open("sample-file.txt")
bigramFrequencyDictionary ={}


for line in inputTextFile:
    line = line.translate(str.maketrans('', '', string.punctuation)).lower()
    lineAsList = [word for word in line.split() if len(word) >= 2]
    for index in range(len(lineAsList)-1):
        bigram = f"{lineAsList[index]} {lineAsList[index+1]}"
        if bigram in bigramFrequencyDictionary.keys():
            bigramFrequencyDictionary[bigram] += 1
        else:
            bigramFrequencyDictionary[bigram] = 1
fiveMostFrequentBigrams = sorted(bigramFrequencyDictionary.items(),key= lambda bigram: bigram[1],reverse=True)[:5]

for bigram in fiveMostFrequentBigrams:
    print(bigram[0],'->',bigram[1])