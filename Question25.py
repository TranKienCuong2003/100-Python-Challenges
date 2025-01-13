class MyClass:
    class_param = "This is a class parameter"
    
    def __init__(self, instance_param=None):
        if instance_param:
            self.instance_param = instance_param
        else:
            self.instance_param = "Default instance parameter"

    def display(self):
        print(f"Class parameter: {MyClass.class_param}")
        print(f"Instance parameter: {self.instance_param}")

obj1 = MyClass("Custom instance parameter")
obj1.display()

obj2 = MyClass()
obj2.display()

print(f"Accessing class parameter from the class: {MyClass.class_param}")
