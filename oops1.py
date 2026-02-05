class employee:
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")


    def travel(self,destination):
        print("This travel method was called manually")
        print(f"Employee is now travellingto {destination}")
# creating an object/instance of the class
sam = employee()




        
# calling a method
sam.travel("jharkhand")


