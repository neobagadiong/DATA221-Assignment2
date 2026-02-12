#given function signature
def find_lines_containing(filename, keyword):

    #start of code
    linesWithMatchedKeyword = []

    #open and read text file
    with open(filename, 'r') as textFile:
        textInFile = textFile.read().splitlines() 
    
    #find lines with matching keywords
    for i in range(len(textInFile)):
        if keyword in textInFile[i].split(): linesWithMatchedKeyword.append((i+1,textInFile[i]))

    return linesWithMatchedKeyword


#test with "Lorem"
testKeywordStats = find_lines_containing('sample-file.txt','Lorem')

#print out 
print(len(testKeywordStats), 'lines found with the matching keyword.')
for line in testKeywordStats[:3]:
    print('Line',line[0],'-',line[1])