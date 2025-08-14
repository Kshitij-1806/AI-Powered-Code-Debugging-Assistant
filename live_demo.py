# live_demo.py - File for live demo with various errors

# 1. Syntax Errors
if x == 5        # Missing colon
    print("Found it")

def broken_function()   # Missing colon
print("No indentation")  # Wrong indentation

# 2. Logic Errors  
while True:              # Infinite loop
    print("Forever")
    # No break condition

def unreachable_example():
    return "done"
    print("This never runs")  # Unreachable code

# 3. Security Issues
user_input = input("Enter code: ")
result = eval(user_input)     # Dangerous eval()

try:
    risky_operation()
except:                       # Bare except
    pass

# 4. Style Issues
_badVariableName = 1         # Leading underscore in Python
myJavaScriptStyle = 2        # camelCase in Python (should be snake_case)

# 5. Structural Issues
def too_many_params(a, b, c, d, e, f, g, h, i, j):  # Too many parameters
    if a:
        if b:
            if c:
                if d:
                    if e:                            # Deep nesting
                        print("Too deep!")

# Duplicate code
print("Hello World")
print("Hello World") 
print("Hello World")
