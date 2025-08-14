# AI-Powered Code Debugging Assistant

A comprehensive AI-powered debugging assistant that automatically identifies, explains, and suggests fixes for various types of code errors.

## 🚀 Features

- **Multi-language Support**: Supports Python, JavaScript, Java, C++, and more
- **Error Classification**: Identifies syntax, logical, structural, performance, and security errors
- **AI-Powered Suggestions**: Provides intelligent fix recommendations
- **Learning Capabilities**: Improves with usage and adapts to coding styles
- **Multiple Interfaces**: CLI, Web dashboard, and Python API
- **Real-time Analysis**: Fast code analysis and feedback

## 📁 Project Structure

```
ai-debugging-assistant/
├── src/
│   ├── analyzers/           # Language-specific analyzers
│   │   ├── python_analyzer.py
│   │   ├── javascript_analyzer.py
│   │   ├── java_analyzer.py
│   │   └── cpp_analyzer.py
│   ├── ai_models/          # Machine learning models
│   │   ├── model_manager.py
│   │   └── suggestion_engine.py
│   ├── cli/                # Command-line interface
│   │   └── main.py
│   ├── web/                # Web dashboard
│   │   ├── app.py
│   │   └── templates/
│   └── core/               # Core debugging logic
│       ├── engine.py
│       ├── error_types.py
│       └── language_detector.py
├── examples/               # Example buggy code files
├── tests/                  # Test files
└── .vscode/               # VS Code configuration
```

## 🛠️ Installation

1. **Clone or download the project**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Usage

### Command Line Interface

1. **Analyze a single file:**
   ```bash
   python -m src.cli.main analyze examples/buggy_python.py
   ```

2. **Analyze with specific output format:**
   ```bash
   python -m src.cli.main analyze examples/buggy_python.py --output table
   ```

3. **Batch analyze multiple files:**
   ```bash
   python -m src.cli.main batch examples/ --pattern "*.py"
   ```

4. **Get detailed explanations:**
   ```bash
   python -m src.cli.main explain examples/buggy_python.py --line 17
   ```

### Web Interface

1. **Start the web server:**
   ```bash
   python src/web/app.py
   ```

2. **Open your browser to:** `http://localhost:5000`

3. **Upload files or paste code directly for analysis**

### Python API

```python
from src.core.engine import DebuggingEngine

engine = DebuggingEngine()
result = engine.analyze_file('your_code.py')

print(f"Found {len(result.errors)} errors")
for error in result.errors:
    print(f"Line {error.line_number}: {error.message}")
```

## 🧪 Testing

Run the test suite with the provided examples:

```bash
python test_assistant.py
```

## 🌟 Supported Languages

- **Python** - Comprehensive syntax, logic, and style analysis
- **JavaScript/TypeScript** - ES6+ features, common pitfalls
- **Java** - Object-oriented best practices, null safety
- **C/C++** - Memory management, buffer overflow detection
- **More languages** - Extensible architecture for adding new analyzers

## 📊 Error Types Detected

### Syntax Errors
- Missing semicolons, brackets, quotes
- Invalid syntax according to language grammar
- Mismatched delimiters

### Logical Errors  
- Infinite loops
- Unreachable code
- Division by zero
- Null pointer exceptions

### Structural Issues
- Deep nesting
- Long functions
- Code duplication
- Poor organization

### Performance Problems
- Inefficient algorithms
- Memory leaks
- Unnecessary computations

### Security Vulnerabilities
- SQL injection risks
- XSS vulnerabilities
- Use of dangerous functions

### Style Issues
- Naming conventions
- Code formatting
- Best practices violations

## 🎯 Example Analysis

**Input Code (buggy_python.py):**
```python
def buggy_function(x, y):
    result = x + y
    print("Result is:", result)
    # Missing return statement

while True:
    print("Infinite loop!")
    # No break condition

result = eval("2 + 2")  # Dangerous function
```

**AI Assistant Output:**
```
🔍 Analysis Results
Language: python
Status: completed
Errors found: 3

1. Line 4: Missing return statement (logical)
2. Line 6: Potential infinite loop detected (logical) 
3. Line 10: Use of eval() is dangerous (security)

💡 AI Suggestions:
- Add return statement to function
- Add break condition to loop
- Replace eval() with safer alternatives
```

## 🚀 VS Code Integration

The project includes VS Code tasks for easy development:

- **Ctrl+Shift+P** → "Tasks: Run Task"
- Choose from:
  - "Run AI Debugging Assistant Test"
  - "Analyze Python Example"
  - "Analyze Java Example"
  - "CLI Help"

## 🔧 Configuration

The assistant can be configured through:
- Environment variables
- Configuration files
- Command-line options
- VS Code settings

## 🤝 Contributing

1. Add new language analyzers by extending `BaseAnalyzer`
2. Implement comprehensive error detection
3. Provide actionable fix suggestions
4. Follow the established error classification system
5. Add appropriate tests and documentation

## 📄 License

MIT License - feel free to use and modify for your projects!

---

**Made with ❤️ for developers who want to write better code faster!**
