# Python naming test
_private_var = 1        # Should be flagged (leading underscore)
myVariable = 2          # Should be flagged (camelCase)
MyClass = 3             # Should be flagged (PascalCase for variable)
__name_mangled = 4      # Should be flagged (name mangling)
normal_var = 5          # This is correct (snake_case)

def test_function():
    return "ok"
