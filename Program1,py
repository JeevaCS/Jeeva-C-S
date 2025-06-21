class Calculator:
    def init(self, a: float, b: float):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero"

    def calculate(self, operation: str):
        operation = operation.lower()
        if operation == "add":
            return self.add()
        elif operation == "subtract":
            return self.subtract()
        elif operation == "multiply":
            return self.multiply()
        elif operation == "divide":
            return self.divide()
        else:
            return "Error: Invalid operation type"
input1=input("please enter first number:")
a=float(input1)
input2=input("please enter second number:")
b=float(input2)
operation=input("please enter operation(add,subtract,multiply,divide):")
