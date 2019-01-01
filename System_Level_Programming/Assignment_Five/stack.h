/*
 * Definitions for Assignment 5
 * CISC 220, Fall 2017
 * M. Lamb
 *
 * Note: There are multiple options for representing stacks in C,
 * like any other language.  For this assignment, we're going to
 * represent stacks as linked lists.  The beginning of the linked
 * list is the top of the stack.
 */

#define TRUE 1
#define FALSE 0


// The maximum length of a string inside a stack.  Ten characters
// plus the obligatory '\0' at the end of the string
#define MAX_STRING_LENGTH 11

/*
 * A structure type for representing a single node for one element of
 * a stack.  Because an element of a stack may be either an integer
 * or a string, there's a union inside the structure.
 * 
 * The name "Stack" is provided with a typedef so that we don't have
 * to type "struct StackNode" all the time -- but you can use
 * "struct StackNode" if you want to.
 */
struct StackNode {
  // intTop is TRUE if the top element is an int.  If the top element
  // is a string, intTop is FALSE.
  int intTop; 

  // The data element will hold either an int or a string,
  // not both!  intTop will tell us which it is.  If it
  // holds a string the length of the string may not be more
  // than MAX_STRING_LENGTH characters (including the '\0' at
  // end end).
  union {
    int intValue;
    char stringValue[MAX_STRING_LENGTH];
  } data;
  
  struct StackNode *next; // a pointer to the next node down in the
                          // stack (or NULL if this is the last node)
};// end struct StackNode

// A synonym for "struct StackNode" to save typing
typedef struct StackNode Stack;

// Headers for all the required functions, which must be implemented in
// stack.c

/*
 * Parameter: a stack
 * Returns TRUE if the stack is empty and FALSE if it's not.
 * Does not change the stack.
 */
int isEmpty(Stack *stack);

/* 
 * This function pushes an integer onto the top of a stack.
 * Parameters: 
 *    1. a stack (NULL or a pointer to the top node)
 *    2. an integer value to push onto the top of the stack
 * Returns a pointer to the start of the modified stack.
 */
Stack *pushInt(Stack *stack, int value);

/*
 * Parameter: a stack
 * Prints the stack to the standard output from top to bottom, 
 * in a format like this: 
 *    [1,2,"apple","computer",17,"Queens"]
 * The values are enclosed in square brackets and separated
 * by commas, with no spaces.  There are quotes around the 
 * string values so that the user can tell the difference between
 * the number 42 and the string "42".
 * The stack is printed on one line, followed by an end-of-line
 * character.  If the stack is empty the output is "[]", followed 
 * by an end of line character.
 */
void printStack(Stack *stack);

/*
 * This function pushes a string onto the top of a stack.
 * Parameters: 
 *    1. a stack (NULL or a pointer to the top node)
 *    2. a string value to push onto the top of the stack
 * Returns a pointer to the start of the modified stack.
 * The string is copied into the stack; the stack will not
 * contain a pointer to the original parameter.
 */
Stack *pushString(Stack *stack, char *value);


/*
 * This function takes a stack as a parameter and returns
 * TRUE if the stack is not empty and its top element is
 * an integer.  Returns FALSE otherwise (i.e. if the stack is
 * empty or its top element is a string).
 */
int topIsInt(Stack *stack);

/*
 * This function takes a stack as a parameter and returns
 * TRUE if the stack is not empty and its top element is
 * a string.  Returns FALSE otherwise (i.e. if the stack is
 * empty or its top element is an integer).
 */
int topIsString(Stack *stack);

/*
 * This function returns the value of the "top" element of a 
 * stack if that value is an integer.  Does not change the stack.
 * If this function is called when the stack is empty or when the
 * top element is a string, it writes an error message and returns
 * 0.
 */
int topInt(Stack *stack);

/*
 * This function copies the "top" string of a stack into a 
 * string supplied by the caller.  The supplied string MUST
 * have enough room for MAX_STRING_LEN characters plus the
 * ending '\0'.  Does not change the stack. 
 * 
 * If this function is called when the stack is empty or when
 * the top element is an integer, it writes an error message
 * and copies an empty string into the second parameter (i.e.
 * sets its first character to '\0').
 */
void topString(Stack *stack, char *topString);

/* 
 * This function "pops" the top value off of a stack and returns
 * the modified stack.  If called for an empty stack, writes an 
 * error message and returns the empty stack without changing it.
 * Besides changing the stack, it frees the heap space used by
 * the popped element.
 */
Stack* pop(Stack *stack);

/*
 * This function returns the number of integers in a stack.
 */
int countInts(Stack *stack);

/*
 * This function returns the number of strings in a stack.
 */
int countStrings(Stack *stack);

  


  

