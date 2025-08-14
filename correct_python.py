# Correct Python file
def greet(name):
    """A simple greeting function."""
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")

def calculate(a, b):
    """Calculate sum of two numbers."""
    return a + b

class Person:
    """A simple Person class."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

if __name__ == "__main__":
    # Test the functions
    greet("Alice")
    result = calculate(5, 3)
    print(f"5 + 3 = {result}")
    
    # Test the class
    person = Person("Bob", 25)
    print(person.introduce())
