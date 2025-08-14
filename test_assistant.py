#!/usr/bin/env python3
"""
Test script for the AI debugging assistant.
"""

import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from src.core.engine import DebuggingEngine
from src.core.error_types import ErrorSeverity

def test_debugging_assistant():
    """Test the debugging assistant with example files."""
    print("🤖 AI-Powered Code Debugging Assistant Test")
    print("=" * 50)
    
    engine = DebuggingEngine()
    
    # Test files
    test_files = [
        "examples/buggy_python.py",
        "examples/buggy_javascript.js", 
        "examples/buggy_java.java"
    ]
    
    for file_path in test_files:
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            continue
            
        print(f"\n🔍 Analyzing: {file_path}")
        print("-" * 30)
        
        try:
            result = engine.analyze_file(file_path)
            
            print(f"Language: {result.language}")
            print(f"Status: {result.status.value}")
            print(f"Analysis time: {result.analysis_time:.2f}s")
            print(f"Confidence: {result.confidence_score:.1%}")
            print(f"Total errors: {len(result.errors)}")
            print(f"Suggestions: {len(result.suggestions)}")
            
            # Group errors by severity
            severity_counts = {}
            for error in result.errors:
                severity = error.severity.value
                severity_counts[severity] = severity_counts.get(severity, 0) + 1
            
            print("\nErrors by severity:")
            for severity in ['critical', 'high', 'medium', 'low']:
                count = severity_counts.get(severity, 0)
                if count > 0:
                    print(f"  {severity}: {count}")
            
            # Show first few errors
            if result.errors:
                print("\nTop 3 errors:")
                for i, error in enumerate(result.errors[:3], 1):
                    print(f"  {i}. Line {error.line_number}: {error.message} ({error.error_type.value})")
            
        except Exception as e:
            print(f"❌ Error analyzing {file_path}: {str(e)}")
    
    print("\n✅ Test completed!")

if __name__ == "__main__":
    test_debugging_assistant()
