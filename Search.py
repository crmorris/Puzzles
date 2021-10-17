#value = input("Please enter the word search letters:\n")

tempValue = "catdogant"
#this is a temporary value to test a simpler version first

lengthOfLines = int(input("Please enter the length of each line:\n"))
#this will help me print out the location of the word in a 2d array later

listOfWords = input("Please enter the word you're searching for:\n")
#I would eventually like to do several words at once separated by a space

startPos = 0
#tracks the index of the puzzle string

wordCheck = 0
#tracks the index of the word you're searching for

answers = []
#used to store location of letters

for x in tempValue:
    if listOfWords[wordCheck] == x:
        answers.insert(len(answers) + 1, [startPos % lengthOfLines, int((startPos - startPos % lengthOfLines) / lengthOfLines + 1)])
        #prints one number greater than index for client readability
        wordCheck += 1
    startPos += 1
    if len(answers) == len(listOfWords):
        break
#loops through word search puzzle letters and prints out location of the word you're searching for

print(answers)