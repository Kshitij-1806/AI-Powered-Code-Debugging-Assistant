public class TestClass {
    private int _privateVar = 1;    // Should be flagged (leading underscore)
    private int PascalCaseVar = 2;  // Should be flagged (PascalCase)
    private int snake_case_var = 3; // Should be flagged (snake_case)
    private int normalVar = 4;      // This is correct (camelCase)
    
    public void TestMethod() {      // Should be flagged (PascalCase method)
        int localVar = 5;           // This is correct
    }
}
