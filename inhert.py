# class Animal :
#     def __init__(self,name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name} makes a sound.")
#         # derived class
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks.")


#   ## create an instance of animal
# animal = Animal("Generic Animal")
# animal.speak()
# dog = Dog("Buddy")
# dog.speak()          



## Super Keyword
# Super
# base class
class Animal:
    def __init__(self):
        self.name = "Buddy"
    

    def speak(self):
        print(f"{self.name} makes a sound.")




## Derived Class
class Dog(Animal):
    def __init__(self,breed):
        super().speak()   #call the base class method
        print (f"{self.name} barks . It is a {self.breed}.")

        # create an instance of dog 
dog = Dog("Golden Retriever")
dog.speak()



        