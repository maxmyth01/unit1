#Max Low
#9-1-17
#stringAnalysis.py - Studies a sentance and counts the amount of words letter and scans for a letter and word

sentance = input('Enter a Sentance')
sentance.upper()
space = (' ')
totalWords= (sentance.count(space)+1)
totalCharactures = len(sentance)
totalLetters = (totalCharactures-totalWords-1)


print('Your sentance has', totalWords ,'words and', totalCharactures ,'characters and', totalLetters ,'letters')

letter = input('Enter a character to search for:')

selectLetter = sentance.count(letter)


print('Your sentance has', selectLetter ,'of the character',letter)

word = input('Enter a word to search for:')

selectWord = sentance.count(word)


print('Your sentance has', selectWord ,'of the word',word)


