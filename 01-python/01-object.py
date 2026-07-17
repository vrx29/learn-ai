# Object and Mutability
# Everything is object in python
"""
Each Object has -> Identity, Type, Value

Objects are Mutable and immutable
"""

sugar_amount = 20
print(f"Intial Amount: {sugar_amount}")

# IF I change sugar_amount = 40 it will change the actual amount to verify this alway check with id()

sugar_amount = 40;
print(f"Changed amount: {sugar_amount}")

print(f"Id of 2: {id(20)}")
print(f"Id of 40: {id(40)}")