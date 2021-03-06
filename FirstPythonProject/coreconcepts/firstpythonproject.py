# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import random

if __name__ == "__main__":
    # a simple message from Python program
    print("Hello World")
    # Python variables
    firstStrVar = "First variable"
    secondStrVar = 'Second variable'#another way to define a string
    thirdIntvar = 34
    # concatenate same type variables
    print(firstStrVar+" "+secondStrVar)
    print(thirdIntvar)
    print("==================== using global and local variables ===================")
    # local and global variables
    globalVariableOne = "Global variable without explicit global keyword"
    global globalVariableTwo
    globalVariableTwo = "Global variable with explicit global keyword"
    def concat_str():
        print(globalVariableOne+" "+globalVariableTwo)
    concat_str()
    print("=================== concatenate strings =========================")
    def other_concat_str():
        localVariableOne = "Local variable one"
        localVariableTwo = "Local variable two"
        print(localVariableOne + " " + localVariableTwo)
    other_concat_str()
    print("================== local and global variables ======================")
    def combined_variables_usage():
        localVariable = "Local variable"
        print("Local Variable: "+localVariable)
        globalVariableOne = "Overloaded globalVariableOne"
        print("Global variable one overiden : "+globalVariableOne)
    combined_variables_usage()
    print("Global variable not overiden: "+globalVariableOne)
    print("================== data types and predefined collections ==========================")
    # Python data types
    binarytypeVariable = "Example"
    print("Binary type variable Example:" + binarytypeVariable)
    byteArrayVariable = bytearray(10)
    print("Byte Array variable 10: "+str(byteArrayVariable))
    memoryViewVariable = memoryview(bytes(5))
    print("Memory View variable bytes(5)" + str(memoryViewVariable))
    intNumericalVariable = -30
    print("Numerical int variable: "+str(intNumericalVariable))
    floatNumericalVariable = 234.777
    print("Float number variable: "+str(floatNumericalVariable))
    textVariable = "Text variable"
    print("Text variable: "+textVariable)
    complexNumericalVariable = 3+4j
    print("Complex number variable: "+str(complexNumericalVariable))
    listOfTextVariables = ["One","Two","Three"]
    i=0
    while i<3:
        print("List of variables: "+listOfTextVariables[i])
        i=i+1
    tupleOfTextVariable = ("One","Two","Three")
    for x in tupleOfTextVariable:
        print("Tuple of text variables: "+x)
    rangeVariable = range(6)
    print("Range variable: "+str(rangeVariable))
    dictionaryVariable = {"CNP":"188010212345","NAME":"IRON MAN","AGE":120}
    for y in dictionaryVariable:
        print("Dictionary variable:"+y)
    setVariable = {"apple","blackberry","plum"}
    for z in setVariable:
        print("Set variable: "+z)
    frozensetVariable = ({"frozen apple","frozen blackberry","frozen plum"})
    for t in frozensetVariable:
        print("Frozen set variable:" + t)
    booleanVariable = True
    print("Boolean variable: "+str(booleanVariable))
    print("===================== using type() method ===============================")
    print(type(binarytypeVariable))
    print(type(byteArrayVariable))
    print(type(memoryViewVariable))
    print(type(intNumericalVariable))
    print(type(floatNumericalVariable))
    print(type(complexNumericalVariable))
    print(type(listOfTextVariables))
    print(type(tupleOfTextVariable))
    print(type(rangeVariable))
    print(type(dictionaryVariable))
    print(type(frozensetVariable))
    print(type(booleanVariable))
    print("=================== converting numbers ==========================")
    intNumber = 1 # int
    floatNumber = 2.8 # float
    z = 1j # complex
    #convert from int to float:
    a = float(intNumber)
    #convert from float to int:
    b = int(floatNumber)
    #convert from int to complex:
    c = complex(intNumber)
    # convert from float to complex
    d = complex(floatNumber)
    print("Coverting from int numer "+str(intNumber)+" to float number "+ str(a))
    print("Coverting from float numer "+str(floatNumber)+" to int number "+ str(b))
    print("Coverting from int numer "+str(intNumber)+" to complex number "+ str(c))
    print("Coverting from float numer "+str(floatNumber)+" to complex number "+ str(d))
    print("====================== using random module =============================")
    randomIntNumber = random.randrange(1,6)
    randomFloatNumber = random.randrange(1.0,10.0)
    print("Integer random generated number = "+str(randomIntNumber))
    print("Float random generated number = "+str(randomFloatNumber))
    print("====================== using strings ========================")
    stringVariableOne = 'One string'
    stringVariableTwo = "Second string"
    stringVariableTheLongOne = """This is a long string 
    defined on multiple lines 
    of code"""
    stringAnotherVeryLongString='''Another very long string 
    defined on multiple lines 
    of code '''
    intNumberToConvertToString = -233
    convertedStringFromAnIntNumber = str(intNumberToConvertToString)
    floatNumberToConvertToString = -14.887
    convertedStringFromAFloatNumber = str(floatNumberToConvertToString)
    print(stringVariableOne)
    print(stringVariableTwo)
    print(stringVariableTheLongOne)
    print(stringAnotherVeryLongString)
    print("String converted from an integer number = "+convertedStringFromAnIntNumber)
    print("String converted from a float number = " + convertedStringFromAFloatNumber)
    print("======================== format strings ==============================")
    firstString = "Do not enter if your age is under" 
    secondString = " 18."
    thirdString = firstString+" {}."
    age=18
    print(firstString+secondString)
    print(thirdString.format(age))
    sell2Coffees = 2
    sell3Coffees = 3
    priceForTwoCoffees = 10
    priceForThreeCoffees = 12    
    messageString = """Today we sell {2} coffees for just {0} dollars. 
    For {3} coffees you\"l pay, just today, {1} dollars."""
    print(messageString.format(priceForTwoCoffees,priceForThreeCoffees,
    sell2Coffees,sell3Coffees))
    print("Just a quote form Sheakspeare: \" To be or not to be.\"")
    print("===================== using Booleans ================================")
    justAString = "Just a string"
    print(isinstance(justAString,str))
    print(isinstance(justAString,int))
    print(bool(""))
    oneArray = []
    print(bool(oneArray))
    oneList = {}
    print(bool(oneList))
    floatNumber = 8.7
    print(bool(floatNumber))
    intNumber = 0
    print(bool(intNumber))
    dictionaryOne = {10:2,11:8,23:89}
    print(bool(dictionaryOne))
    print("================== using few numerical operators ==================")
    operandOne = 2
    operandTwo = 3
    result = operandOne+operandTwo
    resultString=str(result)
    print("2+3="+resultString)
    result = operandOne-operandTwo
    resultString=str(result)
    print("2-3="+resultString)
    result = operandOne*operandTwo
    resultString=str(result)
    print("2*3="+resultString)
    result = operandOne/operandTwo
    resultString=str(result)
    print("2/3="+resultString)
    result = operandOne//operandTwo
    resultString=str(result)
    print("2//3="+resultString)
    result = operandOne%operandTwo
    resultString=str(result)
    print("2%3="+resultString)
    result = operandOne**operandTwo
    resultString=str(result)
    print("2**3="+resultString)
    print("======================== using lists ==============================")
    thislist = ["apple", "banana", "cherry"]
    print("First element of list is: "+thislist[0])
    print("Last element of list is:"+thislist[-1])
    thislist.append("plum")
    print("After adding plum to list, content of list is: ")
    print(thislist)
    thislist.insert(3,"orange")
    print("After inserting at index 3 organge in list, content of list is: ")
    print(thislist)
    print("Using a for...in...: to list all elements of list")
    for currentelelementoflist in thislist:
        print(" Elementul curent al listei este: " + currentelelementoflist)
    print("Deleting last element of list")
    thislist.pop()
    print(thislist)
    print("Deleting fist element of list")
    thislist.pop(0)
    print(thislist)
    print("create a new list from initial list")
    newlist = list(thislist)
    print(newlist)
    print("Insert new list at index 1 of old list")
    thislist.insert(1,newlist)
    print(thislist)
    print("======================== using tuples ==============================")
    thistuple = ("apple", "banana", "cherry")
    print("First element of tuple is: "+thistuple[0])
    print("Last element of tuple is:"+thistuple[-1])
    print("Using a for...in...: to tuple all elements of tuple")
    for currentelelementoftuple in thistuple:
        print(" Elementul curent al tuplei este: " + currentelelementoftuple)
    print("create a new tuple from initial tuple")
    newtuple = tuple(thistuple)
    print(newtuple)
    print("======================== using sets ==============================")
    thisset = {"fruts","tomato"}
    thisset.add("apple")
    thisset.add("banana")
    thisset.add("cherry")
    thisset.add("plum")
    print("After adding plum to set, content of set is: ")
    print(thisset)
    print("Add lemon, cherry and nuts to set")
    thisset.update(["lemon","cherry","nuts"])
    print(thisset)
    print("Using a for...in...: to set, all elements of list are:")
    for currentelelementofset in thisset:
        print(" Elementul curent al setului este: " + currentelelementofset)
    print("Deleting apple from set")
    thisset.remove("apple")
    print(thisset)
    print("Deleting last element of set")
    thisset.pop()
    print(thisset)
    print("create a new set from initial list")
    newset = set(thisset)
    print(newset)
    print("======================== using dictionaries ==============================")
    thisdictionary = {"first":"apple", "second":"banana", "third":"cherry"}
    print("First element of disctionary is: "+thisdictionary["first"])
    print("Changing element with key three with value plum:")
    thisdictionary["forth"]="plum"
    print("After adding plum to list, content of disctionary is is: ")
    print(thisdictionary)
    print("Using a for...in...: to list all elements (key,value) of dictionary")
    for currentelelementofdisctionarykey, currentelementofdictionaryvalue in thisdictionary.items():
        print(" Key of current element of dictionary is: " + currentelelementofdisctionarykey)
        print(" Value of current element of dictionary is: " + currentelementofdictionaryvalue)
    print("Deleting second key element of list")
    thisdictionary.pop("second")
    print(thisdictionary) 
    print("====================using if statement ================================")
    username = input("Enter username:")
    print("Username is: " + username)
    password = input("Enter password:")
    print("Password is: " + password)  
    if "utilizator" == username:
        if "parola" == password:
            print("Username and password are both ok!")
        else:
            print("Username is ok but password is not!")
    else:
        print("Username is not ok!")
    print("====================using while statement ================================")
    i = 0
    while i < 8:
        print(i)
        i += 1
        if i==4: continue
    else:
        print("i is no longer less than 8. i="+str(i))
        i=i+10
    print("i="+str(i))
    print("======================== using for statement ===========================")
    collection = ("one","two","three","four","five","six")
    s1 = "three"
    s2 = "five"
    for element in collection:
        if element == s1:
            print("value three is here")
            continue
        if element == s2:
            print("value five is here")
            break
        print("current element is: "+element)    
    else:
        print("Else element is:"+element)
    for currentElement in collection:
        print("Current element of collection is: "+currentElement)
    print("================= using functions  =============================")
    # define function computing with 3 parameters
    # operation : = - * or /
    # operand1  number 
    # operand2  number
    def computing(operation,operand1,operand2):
        result =0.0
        if "+" == operation:
            result = operand1 + operand2
        else:
            if "-" == operation:
                result = operand1 + operand2
            else:
                if "*" == operation:
                    result = operand1 * operand2
                else:
                    if "/" == operation:
                        result = operand1 / operand2
                    else:
                        print("Wrong operation! You have to use: + or - or * or/")
        print(str(operand1)+" "+ str(operation) + " " + str(operand2) + " = " + str(result))
    #call 4 times computing unction
    computing("+",20.4,50.3)
    computing("-",50.5,30.4)
    computing("*",20.4,50.3)
    computing("/",50.5,30.4)
    print("================= using lambda functions  =============================")
    # define lambda functions computing with 3 parameters
    # operation : = - * or /
    # operand1  number 
    # operand2  number
    add = lambda x,y : x+y
    print("Result lambda add is: "+str(add(20,50.3)))
    substract = lambda x,y : x-y
    print("Result lambda substract is: "+str(substract(50.5,30.4)))
    multiply = lambda x,y : x*y
    print("Result lambda multiply is: "+str(multiply(20.4,50.3)))
    divide = lambda x,y : x/y
    print("Result lambda divide is: "+str(divide(50.5,30.4)))
    print("================= using classes  =============================")  
    # define class SpaceCoordinate
    class SpaceCoordinate:
        xCoordinate = 0.0
        yCoordinate = 0.0
        zCoordinate = 0.0
        # class constructor
        def __init__(self, x,y,z):
            self.xCoordinate = x
            self.yCoordinate = y
            self.zCoordinate = z
        # class coordinates printing function
        def print_space_point(self):
            print("x coordinate = "+str(self.xCoordinate))
            print("y coordinate = "+str(self.yCoordinate))
            print("z coordinate = "+str(self.zCoordinate))
    #create two objects or instances of class SpaceCoordinate
    spacePoint = SpaceCoordinate(10.0,11.0,12.0)
    spacePointOne = SpaceCoordinate(0.0,12.9,33.0)
    # call print_space_point(self) fnction of created objects 
    SpaceCoordinate.print_space_point(spacePoint)
    SpaceCoordinate.print_space_point(spacePointOne)
    print("=================== using class inheritance ===========================") 
    class Person:
        id = "000000000000"
        surname = "default surname"
        name = "default name"
        #class constructor
        def __init__(self, id,surname,name):
            self.id = id
            self.surname = surname
            self.name = name
        #class print_person function
        def print_person(self):
            print("Person id: "+str(self.id))
            print("Person surname: "+str(self.surname))
            print("Person name: "+str(self.name))
    class Employee(Person):
        employeeID = "CDDD_YYYY"
        employeeSalary = 0
        #class constructor
        def __init__(self, id, surname, name, employeeID,employeeSalary):
            Person.__init__(self,id,surname,name)
            self.employeeID = employeeID
            self.employeeSalary = employeeSalary
        def print_employee(self):
                Person.print_person(self)
                print("Employee ID: "+self.employeeID)
                print("Employee salary: "+str(self.employeeSalary)) 
    #create John Doe and Jane Doe persons and print their details
    secondPerson = Person("1234567890123","John","Doe")
    firstPerson = Person("1234567890111","Jane","Doe")
    Person.print_person(firstPerson)
    Person.print_person(secondPerson)
    # employ John Doe and Jane Doe and print their details
    firstEmployee = Employee(firstPerson.id,firstPerson.surname,firstPerson.name,"211_2019",120000)
    secondEmployee = Employee(secondPerson.id,secondPerson.surname,secondPerson.name,"212_2019",140000)
    Employee.print_employee(firstEmployee)
    Employee.print_employee(secondEmployee)
    print("======================= using iterators ==========================") 
    mytuple = ("one", "two", "three") #create a tuple
    myit = iter(mytuple)    #create an iterator of the tuple we created
    print(next(myit))   # call netx method
    print(next(myit))
    print(next(myit))
    mystr = "each letter"
    myit = iter(mystr)
    print(next(myit))
    print(next(myit))
    print(next(myit))
    print(next(myit))
    print(next(myit))
    print(next(myit))
    print(next(myit))
    print(next(myit))
    print(next(myit))
    print(next(myit))
    print(next(myit))
    print("=========================== using modules =========================") 
    import person
    
    firstPerson = Person("123126912345","John","Doe")
    secondPerson = Person("244126912345","Jane","Doe")
    firstPerson.print_person()
    secondPerson.print_person()
    print("dir() method returns: "+str(dir(person)))
    print("====================== using date and time ========================") 
    import datetime
    
    x = datetime.datetime.now()
    print("Date and time now:" + str(x))
    year = x.year
    print("Actual year is "+str(year))
    x = datetime.datetime(2018, 6, 1)
    print(x.strftime("%A"))
    print(x.strftime("%B"))
    print(x.strftime("%w"))
    print(x.strftime("%y"))
    print(x.strftime("%j"))
    print(x.strftime("%U"))
    print("======================= using JSON ================================") 
    import json
    # some JSON:
    jsonString =  '{ "name":"John", "age":30, "city":"New York"}'
    # parse x:
    convertedJSONString = json.loads(jsonString)
    # the result is a Python dictionary:
    print("name: "+ str(convertedJSONString["name"]))
    print("age: " + str(convertedJSONString["age"]))
    print("city:"+ str(convertedJSONString["city"]))
    dictionary = {
      "name": "John",
      "age": 30,
      "children": ("Ann","Billy"),
      "pets": None,
      "cars": [
        {"model": "BMW 230", "mpg": 27.5},
      ]
    }
    print("Dictionary converted to JSON format is: "+json.dumps(dictionary))
    print("========================== regular expressions =====================")
    import re
    
    txt = "Rat 123 ta 1 ta ta 44 ta rat ta 55 tata rat 678 rat rat ta ta 2 tata"
    x = re.findall("Rat", txt)
    y = re.findall("rat", txt)
    z = re.findall("ta", txt)
    print("Searching Rat result is: "+str(x))
    print("Searching rat result is: "+str(y))
    print("Searching ta result is: "+str(z))
    r = re.findall("^ta", txt)
    print("String starts with \'ta\': "+str(r))
    t = re.findall("tata$", txt)
    print("String ends with \'tata\': "+str(t))
    u = re.findall("tata*", txt)
    print("String contains 0 or more more \'tata\': "+str(u))
    s = re.findall("ta+", txt)
    print("String contains 1 or more more \'ta\': "+str(s))
    v = re.findall("\ARat",txt)
    print("String starting with sequence \'Rat\': "+str(v))
    d = re.findall("\d",txt)
    print("String contains digits: "+str(d))
    e = re.findall("[025]",txt)
    print("String contains digits 0,2 and 5: "+str(e))
    f = re.findall("[t]",txt)
    print("String contains t: "+str(f))
    g = re.findall("[Rt]",txt)
    print("String contains R or t: "+str(g))
    h = re.sub("\s", "_",txt)
    print("Replacing all spaces with _ result is: "+h)
    g = re.split("\s", txt)
    print("Splitting the string in positions of all space chracters" + str(g))
    h = re.split("\s", txt, 2)
    print("Splitting the string in substrings until second positions of space chracters" + str(h))  
    n = re.search("ta", txt)
    print("Display start and end index of first <ta>presence in string = "+str(n.span()))
    print("========================== Exceptions management ======================================")
    # try to open a file and write some text in it. If this will not work a message will be display
    # at the end close the connection to avoid to let the file stream open
    try:
        myfile = open("myfile.txt")
        myfile.write("This is a text written into myfile.txt")
    except:
        print("Something went wrong when writing to the file")
    finally:
        #myfile.close()
        print("This is block finally")
    wait = 0
    while wait < 10:
        wait = wait + 1
        print("wait = "+str(wait))
    """ create and send an exception if a variable x has not required type int 
    variable = "hello"
    if not type(variable) is float:
        raise TypeError("This is not a float number.")
    else:
        print("String is float ?!?!?!?!")
    """
    print("======================= manage user input ============================")
    username = input("Enter username:")
    print("Username is: " + username)
    password = input("Enter password:")
    print("Password is: " + password)