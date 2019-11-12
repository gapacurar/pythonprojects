#create a new text file
global myfile
global text
text = raw_input("Your text to be written into file: ")
try:
    myfile = open("myfile.txt","w+")
    myfile.write(text)
except:
    print("Something went wrong when writing to the file")
finally:
    myfile.close()
    print("This is block finally of creating file")
# open the file for reading
try:
    myfiletoread = open("myfile.txt","r")
    readtext = myfiletoread.read()
    print("Read text: "+readtext)
except:
    print("Something went wrong when reading from the file")
finally:
    myfiletoread.close()
    print("This is block finally of reading file")
