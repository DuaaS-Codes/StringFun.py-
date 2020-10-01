#Author: Duaa Shahzad
#Date: Jan 6th, 2020
#Q1

print("\t\t\t\t StringFun")
strSentence = (str)(input("Enter something: ")) #Prompts user to enter a sentence
print("It has:",len(strSentence), "letters")    #Counts the index of the sentence entered by user
                                         #and outputs result
print("First 5:",strSentence[0:5])              #Counts first 5 letters of the sentence and outputs result
print("Last 5:",strSentence[-5:])               #Counts last 5 letters of the sentence and outputs result
print("Uppercase:",strSentence.upper())         #Converts all letters from sentence into uppercase
print("Lowercase:",strSentence.lower())         #Converts all letters from sentence into lowercase
