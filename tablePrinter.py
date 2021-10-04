# Currently completing Automate The Boring Stuff with Python (2nd Edition)
# Chapter 6: Manipulating Strings, Practice Project 1
# Table Printer

# Input: List of words
# Output: Length of longest word in that list
def longestWordCount(words):
    longestCount = len(words[0])
    for word in words:
        if len(word) >= longestCount:
            longestCount = len(word)
    return longestCount

longestWordCount(['apples', 'oranges', 'cherries', 'banana'])
# >>> 8

# Input: Lists containing lists of words
# Output: An object of the longest words in each list
def lengths(listOfWords):
    listLengths = {}
    listNum = 1
    for list in listOfWords:
        listLengths[str("List " + str(listNum))] = longestWordCount(list)
        listNum += 1
    return listLengths

longestWordCount(['apples', 'oranges', 'cherries', 'banana'])

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

# # >>> {
#     'List 1': 8,
#     'List 2': 5,
#     'List 3': 5
# # }


# Inputs:
#   1: A list containing lists of words
#   2: An object containing the longest words in each list
#   3: An "extra" justification value which adds a little more padding for better presentation
# Output: 
#   A right justified table 
def printTJustified(listOfLists, justifyLength, extra):
    for i in range(len(listOfLists[0])):
        for j in range(len(listOfLists)):
            print((listOfLists[j][i]).rjust(justifyLength[str('List ' + str(j + 1))] + extra), end='')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose'], ['1', '2', '3', '4'], ['suzuki', 'yamaha', 'triumph', 'KTM']]
printTJustified(tableData, lengths(tableData))
