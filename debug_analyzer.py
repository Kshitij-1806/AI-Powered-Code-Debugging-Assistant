#!/usr/bin/env python3
"""Test script to debug analyzer behavior."""

import sys
sys.path.insert(0, '.')

from src.analyzers.python_analyzer import PythonAnalyzer

# Test with obvious syntax error
test_code = '''
# Syntax error - missing colon
if x == 5
    print("x is 5")
'''

print("Testing Python Analyzer directly...")
analyzer = PythonAnalyzer()

print("\n1. Testing syntax analysis:")
syntax_errors = analyzer.analyze_syntax(test_code)
print(f"Found {len(syntax_errors)} syntax errors:")
for error in syntax_errors:
    print(f"  - Line {error.line}: {error.message}")

print("\n2. Testing logic analysis:")
logic_errors = analyzer.analyze_logic(test_code)
print(f"Found {len(logic_errors)} logic errors:")
for error in logic_errors:
    print(f"  - Line {error.line}: {error.message}")

print("\n3. Testing structure analysis:")
struct_errors = analyzer.analyze_structure(test_code)
print(f"Found {len(struct_errors)} structure errors:")
for error in struct_errors:
    print(f"  - Line {error.line}: {error.message}")
