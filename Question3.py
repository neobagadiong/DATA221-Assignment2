import string
inputTextFile = open("sample-file.txt")
normalizedLineDictionary ={}
normalizedLineList = []


for line in inputTextFile:
    normalizedLine = ''.join(line.translate(str.maketrans('', '', string.punctuation)).lower().split())
    if normalizedLine != '':
        normalizedLineList.append(normalizedLine) 
        
for index in range(len(normalizedLineList)):
        if normalizedLineList[index] in normalizedLineDictionary.keys():
            normalizedLineDictionary[normalizedLineList[index]].append(index)
        else:
            normalizedLineDictionary[normalizedLineList[index]] = [index]

multilineLines = []

for key,values in normalizedLineDictionary.items():
    if len(values) >= 2:
        multilineLines.append((key,values))

print(multilineLines[:2])


