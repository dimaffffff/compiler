spec stands for spectacular of course.
This is the specification for GOOSE (Gloriously Overengineered Out of SpitE) Lang (Very creative)
Not exhaustive but this is the bare minimum

[toc]
## SECTION -13.4 - OOP
OOP is not supported in this language and never will be.
The compiler must insult you personally and abort compilation if it finds CLASS keyword in the source file.

## SECTION 1x10^-84 - Output
The output program must only use these python features:  
- variables
- lists
- comparisons
- if/else/elif
- while
- for
- anything from the python standard library that is compatible with non-unix systems

## SECTION 1.23 - Statements
Leaf statements are either function calls or variable mutation.  
Lead statements must be separated with ;  
Compound statements hold multiple statements and are defined like:  
{ INNER STATEMENTS }  
The definition can spread across multiple lines and is not whitespace sensitive.  
Statements may have return values by using the RETURN keyword, in that case you must declare its type like this:
type { INNER_STATEMENTS_WITH_A_RETURN }  
For example:  
INT { RETURN 1; }

## SECTION 2 - Function calls
Function calls should have this syntax:  
function_name argument1 argument2 ...

## SECTION 3x10^8 - Language provided symbols
Any symbol that is provided by the language (standard library, compiler provided symbols) must be all-caps, for example:  
PRINT "hello world"  
INPUT "how are you doing? "  

## SECTION 4 - Functions and scope
### FUNCTIONS
Functions have a list of arguments, a return type, and a compound statement, they are defined like:  
FUNC return_type function_name (arg1,arg2) { STATEMENTS }  
For example:  
FUNC FLOAT calculateArea (width,height) {  
FLOAT area = width * height;
RETURN area;
}  

### SCOPE
A variable declared(see section 5) in a function must never be accessed by a different function.

### LIFETIMES
Accessing a variable that was declared in a function call that has finished executing is undefined behaviour.

## SECTION 5 - Variables
### DECLARATION
Variables cannot change their types, but the compiler may not have any runtime checks.  
A variable name should only contain characters from the english alphabet.  
A variable should be declared like this:  
LET type variable_name  
For example:  
LET INT index  

### MUTATION
You may mutate a variable with this syntax:  
variable_name = new_value  
You can also initiate the variable at declaration with:  
LET variable_declaration = initial_value  
For example:  
LET INT index = 0  
You also can increment any integer or float variable by 1 with this syntax:  
variable_name++  

## SECTION 5.59 - Globals 
Global declarations are managed by the preprocessor(see section 6) and have this syntax:  
#GLOBAL variable_declaration

## SECTION 6 - Preprocessor
The preprocessor will execute before the compiler and has those responsibilities:
- Global variable declaration
- Struct declaration (see section 7)
- Macros

## SECTION 7 - Structs
### DECLARATION
Structs must be declared at the top level with this syntax:  
#STRUCT struct_name (field1_type field1_name = field1_initial_value, field2_type field2_name = field2_initial_value)
For example
#STRUCT position (
FLOAT x = 0
FLOAT y = 0
)

### CREATION
To create a struct variable you have to use this syntax:  
STRUCT struct_name variable_name  
For example:  
STRUCT position playerPos  

### ACCESS
To access a field in a struct variable you have to use this syntax:  
variable_name.field_name  
For example:  
playerPos.y++
