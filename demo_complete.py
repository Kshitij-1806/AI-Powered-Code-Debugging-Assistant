#!/usr/bin/env python3
"""
Complete demonstration of the AI-Powered Code Debugging Assistant.
This script showcases all the main features and capabilities.
"""

import sys
import os
import time
from pathlib import Path

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from src.core.engine import DebuggingEngine
from src.core.error_types import ErrorSeverity, ErrorType

def print_banner():
    """Print a fancy banner."""
    print("=" * 80)
    print("🤖 AI-POWERED CODE DEBUGGING ASSISTANT - COMPLETE DEMONSTRATION")
    print("=" * 80)
    print("Automatically identifies, explains, and suggests fixes for code errors")
    print()

def analyze_example_file(file_path, language_name):
    """Analyze a single example file and display results."""
    print(f"🔍 ANALYZING {language_name.upper()} CODE")
    print("-" * 50)
    print(f"File: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return
    
    try:
        engine = DebuggingEngine()
        start_time = time.time()
        result = engine.analyze_file(file_path)
        
        # Display basic stats
        print(f"✅ Analysis completed in {result.analysis_time:.2f} seconds")
        print(f"📋 Language detected: {result.language}")
        print(f"🎯 Confidence score: {result.confidence_score:.1%}")
        print(f"🐛 Total errors found: {len(result.errors)}")
        print(f"💡 AI suggestions generated: {len(result.suggestions)}")
        
        # Group errors by severity
        severity_counts = {}
        type_counts = {}
        
        for error in result.errors:
            severity = error.severity.value
            error_type = error.error_type.value
            
            severity_counts[severity] = severity_counts.get(severity, 0) + 1
            type_counts[error_type] = type_counts.get(error_type, 0) + 1
        
        # Display severity breakdown
        if severity_counts:
            print("\n📊 ERRORS BY SEVERITY:")
            severity_emojis = {
                'critical': '🚨',
                'high': '⚠️',
                'medium': '⚡',
                'low': 'ℹ️'
            }
            
            for severity in ['critical', 'high', 'medium', 'low']:
                count = severity_counts.get(severity, 0)
                if count > 0:
                    emoji = severity_emojis.get(severity, '•')
                    print(f"  {emoji} {severity.title()}: {count}")
        
        # Display error type breakdown
        if type_counts:
            print("\n🏷️ ERRORS BY TYPE:")
            type_emojis = {
                'syntax': '🔤',
                'logical': '🧠',
                'structural': '🏗️',
                'performance': '⚡',
                'security': '🔒',
                'style': '🎨'
            }
            
            for error_type, count in sorted(type_counts.items()):
                emoji = type_emojis.get(error_type, '•')
                print(f"  {emoji} {error_type.title()}: {count}")
        
        # Show top 5 errors with details
        if result.errors:
            print("\n🔍 TOP ISSUES FOUND:")
            top_errors = sorted(result.errors, key=lambda x: x.severity.value, reverse=True)[:5]
            
            for i, error in enumerate(top_errors, 1):
                severity_colors = {
                    'critical': '🚨',
                    'high': '⚠️',
                    'medium': '⚡',
                    'low': 'ℹ️'
                }
                icon = severity_colors.get(error.severity.value, '•')
                
                print(f"\n  {i}. {icon} Line {error.line_number}: {error.message}")
                print(f"     Type: {error.error_type.value} | Severity: {error.severity.value}")
                
                if error.suggested_fix:
                    print(f"     💡 Fix: {error.suggested_fix}")
        
        # Show AI suggestions
        if result.suggestions:
            print("\n🤖 AI SUGGESTIONS:")
            for i, suggestion in enumerate(result.suggestions[:3], 1):
                title = suggestion.get('title', 'Code Improvement')
                description = suggestion.get('description', 'No description available')
                confidence = suggestion.get('confidence', 0.5)
                
                print(f"\n  {i}. {title}")
                print(f"     {description}")
                print(f"     Confidence: {confidence:.1%}")
        
        print("\n" + "=" * 60)
        
    except Exception as e:
        print(f"❌ Error analyzing {file_path}: {str(e)}")
        print()

def demonstrate_cli_features():
    """Demonstrate CLI features."""
    print("\n🖥️ COMMAND LINE INTERFACE FEATURES")
    print("-" * 50)
    print("The debugging assistant includes a powerful CLI with the following commands:")
    print()
    
    cli_features = [
        ("analyze", "Analyze a single file with multiple output formats"),
        ("batch", "Analyze multiple files in a directory"),
        ("explain", "Get detailed explanations for specific errors"),
        ("fix", "Apply AI-suggested fixes (preview mode)")
    ]
    
    for command, description in cli_features:
        print(f"  📝 {command:10} - {description}")
    
    print("\n📋 Example CLI commands:")
    print("  python -m src.cli.main analyze examples/buggy_python.py")
    print("  python -m src.cli.main analyze examples/buggy_python.py --output table")
    print("  python -m src.cli.main batch examples/ --pattern '*.py'")
    print("  python -m src.cli.main explain examples/buggy_python.py --line 17")

def demonstrate_capabilities():
    """Demonstrate the full capabilities of the system."""
    print("\n🌟 SYSTEM CAPABILITIES")
    print("-" * 50)
    
    capabilities = [
        ("Multi-Language Support", "Python, JavaScript, Java, C/C++, and extensible for more"),
        ("Error Detection", "Syntax, logical, structural, performance, and security issues"),
        ("AI-Powered Analysis", "Intelligent suggestions based on error context and patterns"),
        ("Multiple Interfaces", "CLI, Web dashboard, and Python API"),
        ("Real-time Processing", "Fast analysis suitable for development workflows"),
        ("Learning System", "Improves with usage and adapts to coding styles"),
        ("VS Code Integration", "Tasks and configuration for seamless development"),
        ("Extensible Architecture", "Easy to add new languages and analyzers")
    ]
    
    for capability, description in capabilities:
        print(f"  ✨ {capability:20} - {description}")

def main():
    """Main demonstration function."""
    print_banner()
    
    # Analyze example files
    examples = [
        ("examples/buggy_python.py", "Python"),
        ("examples/buggy_java.java", "Java"),
        ("examples/buggy_javascript.js", "JavaScript")
    ]
    
    for file_path, language in examples:
        analyze_example_file(file_path, language)
        time.sleep(1)  # Brief pause for readability
    
    # Demonstrate other features
    demonstrate_cli_features()
    demonstrate_capabilities()
    
    print("\n🎉 DEMONSTRATION COMPLETE!")
    print("-" * 50)
    print("The AI-Powered Code Debugging Assistant is ready to help you write better code!")
    print()
    print("🚀 Quick Start:")
    print("  1. Run: python test_assistant.py")
    print("  2. Try CLI: python -m src.cli.main analyze examples/buggy_python.py")
    print("  3. Start web UI: python src/web/app.py")
    print()
    print("💡 Tip: Use VS Code tasks (Ctrl+Shift+P > Tasks: Run Task) for easy access!")
    print("=" * 80)

if __name__ == "__main__":
    main()
