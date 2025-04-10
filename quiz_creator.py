#Import or make a program that creates or edit a file or something that checks a file
import os #using import os to check files in the computer

#Ask the user to input what quiz number they want to create or edit
quiz_number = str(input("Please input what quiz you are going to edit or create Ex.(quiz_#_1.txt): "))
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads") #Using expanduser("~") to make it search home directory and put "Downloads" to find the downlaods folder, and using os.path.join to combines all the paths taken to make it one path
file_path = os.path.join(downloads_folder, quiz_number) #Joining both of them to make the full file path
if os.path.exists(file_path): #To check if the file is there or not
    print(f"{quiz_number}" + " will be opened")

else:
    print(f"{quiz_number}" + " does not exist")

#Ask the user to input their question 
#Ask the user to input four options, and input the correct answer
#Print the input of the user in the text file
#If the user inputs "exit", make the program break and update the file with the new inputs of the user