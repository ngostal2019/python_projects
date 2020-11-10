'''
Description: This code is meant to find the longest word in a given text.
Other: Staline Ngoma
Date: November 09, 2020
Disclaimer: This code is not design to reflect the perfection
'''


text = input("Please insert your text: ")
for char in "-.,?\n":
    newText = text.replace(char, ' ') # replacing characters by spaces all over the text
newText = newText.lower()
wordList = newText.split() # splitting the text to get a list
# print(wordList)
countList = [] # Setting a count list to hold length of each word
##################################################################
# Building a List of numbers made from the length of words
###################################################################################################
for line in wordList:
    lineCount = len(line) # Get the length of each word per line
    countList.append(lineCount)
# print(countList)
#####################################################################################################
# Constructing a new dictionary
#####################################################################################################
dic = {} # Initializing an empty dictionary
for keys in wordList: # Iterating to get keys for dictionary
    for values in countList: # Iterating to get values for dictionary
        dic[keys] = values # Filling the initialized empty dictionary with keys and values
        countList.remove(values) # removing each value after assigning it to the empty dict
        break
#####################################################################################################
# Working on comparison to get the longest word
#####################################################################################################
max_value = max(dic.values())
longestWord = [k for k, v in dic.items() if v == max_value] # Getting the longest key in the set
print(longestWord[0])
