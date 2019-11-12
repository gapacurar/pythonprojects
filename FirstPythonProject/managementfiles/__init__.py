#create a new text file
global myfile
global text
text = raw_input("Your text to be written into file: ")
try:
    myfile = open("myfile.txt","w+")
    myfile.write(text+"\n")
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
# adding 4 lines of text into an existing file
try:
    myfile = open("myfile.txt","a+")
    myfile.write("This is first line of text.\n")
    myfile.write("This is second line of text.\n")
    myfile.write("This is third line of text.\n")
    myfile.write("This is fourth line of text.\n")
except:
    print("Something went wrong when writing to the file")
finally:
    myfile.close()
    print("This is block finally of writing to file more lines file")
# read first 10 characters from the file and print them
try:
    myfiletoread = open("myfile.txt","r")
    readtext = myfiletoread.read(10)
    print("Read 10 characters: "+readtext)
except:
    print("Something went wrong when reading 10 charcaters from the file")
finally:
    myfiletoread.close()
    print("This is block finally of reading 10 charcaters from file")
# read first line from the file and print them
try:
    myfiletoread = open("myfile.txt","r")
    firstline = myfiletoread.readline()
    print("First line: "+firstline)
    """
    for line in myfiletoread:
        line = myfiletoread.readline()
        print("Line: "+line)"""
except:
    print("Something went wrong when reading first line from the file")
finally:
    myfiletoread.close()
    print("This is block finally of reading lines of file")
# read line by line from the file and print them
try:
    myfiletoreadlines = open("myfile.txt","r")
    for line in myfiletoreadlines:
        print("Line: "+line)
except:
    print("Something went wrong when reading line by line from the file")
finally:
    myfiletoreadlines.close()
    print("This is block finally of reading line by line of file")