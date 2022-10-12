import os
import csv 

#The below line is used to open a text file in reading format
#we have various different formats of opening a file in python r,w,a(read,write,append)

fileOpen=open("tempFile.txt","r")
fileOpen.read()
#this function is used to read the contents of the text file
#We can also specify the number of content we want to read inside the read() method

#we can also read a text file line by line using the readline function

fileOpen.readline()
contentFile=file.readlines()
#The readlines functions read all the lines in the file and returns a list of all the lines in the file
#We can also loop through the lines in a file to read it
#A delimiter is a character or a symbol which is used to describe the divison of the content in the content
#By default the delimiter in the lines for the content of the file is \n that is \n seperates the lines in a file in python

for x in fileOpen:
    print(x)
   
#We need to close the fileHandler that we have opened above

fileOpen.close()

f=open('C:\myfile.txt')
while True:
    try:
        line=next(f)
        print(line)
    except StopIteration:
        break
f.close()

#The difference between append and write mode in python is that w mode overwrites an existing file
#Whereas the append mode writes more content to an existing file
#Both methods will create a new file if the file that you have mentioned doesn't exists

fileHandler=open("tempText2.txt",'w')

fileHandler.write("I am Kannav ")
#the write() function writes the content that you have mentioned in the brackets to the text file
#the writelines() function is used to write mutiple lines in a file , this is generally done by including all the lines in a list and seperating them by a delimiter that is in this case '\n'
list=["this is kannav \n","fhagfafgjagh \n"]
fileHandler.writelines(list)


# to delete a file in the system we use the os module
os.remove("tempFile.txt")



#to read a binary file open the file in the mode rb

fileHandlerBinary=open("tempTxt.png","rb")
print(fileHandlerBinary.read())
fileHandlerBinary.close()

#to write to a binary file we open it in the mode wb
fileHandlerBinary=open("tempTxt.png","wb")
#pickling -TO DO


#CSV FILE HANDLING
# Csv files are those files which are seperated by comma ,"comma seperated values"

with open("tempCSV.csv",'r') as csvFileHandler:
    fileReader=csv.reader(csvFileHandler)
    # reader is a function which is used to read and handle the content of a csv file 
    # next() function returns the current row and moves onto the next row
    header=next(fileReader)
    for rows in fileReader:
        print(rows)