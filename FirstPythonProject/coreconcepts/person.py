# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    class Person:
        id="0000000000000"
        name="default name"
        surname="default surname"
        #constructor
        def __init__(self,id,name,surname):
            self.id=id
            self.name=name
            self.surname=surname
        # print person function
        def print_person(self):
            print("person id = " + id)
            print("person name = " + name)
            print("person surname = " + surname)