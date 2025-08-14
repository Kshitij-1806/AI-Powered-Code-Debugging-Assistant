#include <iostream>
using namespace std;

int main() {
    int _x = 1;       // Should be flagged - starts with underscore
    int __reserved;   // Should be flagged - double underscore  
    int SHOUTING = 5; // Should be flagged - all uppercase
    int normalVar = 10; // This is fine
    
    print(_x);
    return 0;
}
