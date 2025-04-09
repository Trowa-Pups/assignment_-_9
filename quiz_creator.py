#Import or make a program that creates or edit a file or something that checks a file
import os #using import os to check files in the computer

#Ask the user to input what quiz number they want to create or edit
quiz_number = str(input("Please input what quiz you are going to edit or create Ex.(quiz_#_1.txt): "))

if os.path.exists(quiz_number):
    print(f"{quiz_number}" + "will be opened")

else:
    print(f"{quiz_number}" + " does not exist")

#Ask the user to input their question 
#Ask the user to input four options, and input the correct answer
#Print the input of the user in the text file
#If the user inputs "exit", make the program break and update the file with the new inputs of the user