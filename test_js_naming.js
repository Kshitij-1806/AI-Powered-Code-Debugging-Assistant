// JavaScript naming test
let _private_var = 1;     // Should be flagged (leading underscore)
let snake_case_var = 2;   // Should be flagged (snake_case)
var CONSTANT_VAR = 3;     // Should be flagged (not const)
const REAL_CONSTANT = 4;  // This is correct
let normalVar = 5;        // This is correct (camelCase)

function testFunction() {
    return "ok";
}
