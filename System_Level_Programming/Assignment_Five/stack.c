/*
 * A skeleton version of the stack module required for 
 * Assignment 5.  It contains all of the required functions,
 * but their bodies are empty and just return arbitrary
 * values of the right type to make the module compile.
 *
 * Your job is to fill in the bodies
 * of the functions.  Adding helper functions is fine
 * too if you want to do that.
 *   
 * A stack that can contain both integers and
 * strings, implemented using a linked list.
 *
 * Comment: TRUE and FALSE are values declared in the 
 * C standard libaries.  TRUE is a non-zero integer
 * and FALSE is zero.
 * 
 * CISC 220, Fall 2017
 * M. Lamb
 * Updates Performed on December 1, 2017 by Michael Krakovsky.
 */

#include "stack.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * Parameter: a stack
 * Returns TRUE if the stack is empty and FALSE if it's not.
 * Does not change the stack.
 */
int isEmpty(Stack *stack) {
  // Note: TRUE and FALSE are constants for 1 and 0, defined
  // in the C standard libraries.
    if (stack != NULL)  {  //if the pointer is null, return TRUE
        return FALSE;
    } else {          
        return TRUE; 
    }
} // isEmpty

/* 
 * This function pushes an integer onto the top of a stack.
 * Parameters: 
 *    1. a stack (NULL or a pointer to the top node)
 *    2. an integer value to push onto the top of the stack
 * Returns a pointer to the start of the modified stack.
 */
Stack *pushInt(Stack *stack, int value) {
    
    Stack* topNode = malloc(sizeof(Stack));   //create a new stack element 
    topNode->data.intValue = value;    
    topNode->intTop = TRUE;        //indicate there is an int
 
    if(isEmpty(stack) == TRUE) {   //if the stack is empty, return the location of the current stack
	topNode->next = NULL;     //the next node is officially a Null
        return topNode;
    } else if (isEmpty(stack) == FALSE) {
        topNode->next = stack;    //The previous top is now the next node
	return topNode;
    } else {
        printf("An error as occured when attempting to push the int.\n");
        return NULL;    //the return of a null indicates a failed attempt
    }
} // end pushInt

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
void printStack(Stack *stack) {
    
    if (isEmpty(stack) == TRUE) {
        printf("[]");                 //print if the linked list is empty
    } else {
        printf("["); //print an open bracket 
        Stack* currentNode;
    	currentNode = stack; 

        while (currentNode->next != NULL) {   //end the loop if you are on the last node
            if (currentNode->intTop == TRUE) {            //print an int or string depending on the value of intTop
                printf("%d", currentNode->data.intValue);
	    } else {
                printf("\"%s\"", currentNode->data.stringValue);
	    }
            currentNode = currentNode->next;   //move to the next stack
            printf(",");  //print a comma
        }  
	if (currentNode->intTop == TRUE) {            //print the last element in the loop with a closed bracket
            printf("%d", currentNode->data.intValue);
        } else {
            printf("\"%s\"", currentNode->data.stringValue);
	}
        printf("]");     //print the close bracket            
    }
} // end printList

/*
 * This function pushes a string onto the top of a stack.
 * If the string would need more than MAX_STRING_LENGTH
 * characters (including the '\0' at the end) it is
 * truncated.  For example, since MAX_STRING_LENGTH is 11,
 * if we try to put the string "ABCDEFGHIJKLMNOP" into the
 * stack this function will copy only "ABCDEFGHIJ" (plus 
 * an ending '\0') into the new stack node.
 *
 * Parameters: 
 *    1. a stack (NULL or a pointer to the top node)
 *    2. a string value to push onto the top of the stack
 * Returns a pointer to the start of the modified stack.
 * The string is copied into the stack; the stack will not
 * contain a pointer to the original parameter.
 */
Stack *pushString(Stack *stack, char *value) {

    Stack* newTop = malloc(sizeof(Stack));  //the return value to the new stack
    newTop->intTop = FALSE;     //indicate a string is present
   
    if (strlen(value) > 10) {     //truncate string if the size is greater then 10 
        newTop->data.stringValue[MAX_STRING_LENGTH - 1] = '\0';   //add a null character at the end of the line
        for(int i = 0; i < (MAX_STRING_LENGTH - 1); i++) {    //recopy string into 10 characters
            newTop->data.stringValue[i] = value[i];
        }
    } else {
        strcpy(newTop->data.stringValue, value); 
    }

    if(isEmpty(stack) == TRUE) {   //if the stack is empty, return the location of the current stack
        newTop->next = NULL;
        return newTop; 
    } else if (isEmpty(stack) == FALSE) {
        newTop->next = stack;      
        return newTop;
    } else {
       return NULL;    //the return of a null indicates a failed attempt
    }
} // end pushString

/*
 * Should not be called with an empty string.
 * Takes a stack as a parameter and returns TRUE
 * if its top element is an integer, false if 
 * it's a string.
 */
int topIsInt(Stack *stack) {
    if (stack->intTop == TRUE) {
        return TRUE;
    } else {
        return FALSE;
    }
}

/*
 * This function returns the value of the "top" element of a 
 * stack if that value is an integer.  Does not change the stack.
 * If this function is called when the stack is empty or when the
 * top element is a string, it writes an error message and returns
 * 0.
 */
int topInt(Stack *stack) {
    
    if ((isEmpty(stack) == FALSE) && (topIsInt(stack) == TRUE)) {
        return stack->data.intValue;     
    } else if (isEmpty(stack) == TRUE) {
        printf("Error: The stack is empty.\n"); 
        return 0;   //return 0 if the stack is empty
    } else {
        printf("Error: The top of the stack is not an int.\n");    
        return 0;   //return 0 if the top is not an integer
    }
} // end topInt

/*
 * This function copies the "top" string of a stack into a 
 * string supplied by the caller.  The supplied string MUST
 * have enough room for MAX_STRING_LEN characters plus the
 * ending '\0'.  Does not change the stack. 
 * 
 * If this function is called when the stack is empty or when
 * the top element is an integer, it writes an error message and
 * puts an empty string into the result parameter.
 */
void topString(Stack *stack, char *result) {
    
    if (strlen(result) > MAX_STRING_LENGTH) {
        strcpy(result, "");
        printf("You have submitted a string that is two small for topString Function.\n");
    } else if ((topIsInt(stack) == TRUE) || (isEmpty(stack) == TRUE)) {
        strcpy(result, "");
        printf("The top of the function is an int or empty. topString Function did not work.\n");
    } else {      
        strcpy(result, stack->data.stringValue);   //copy the result if there is a string and struct is not empty
    }
} // end topString

/* 
 * This function "pops" the top value off of a stack and returns
 * the modified stack.  If called for an empty stack, writes an 
 * error message and returns the empty stack without changing it.
 * Besides changing the stack, it frees the heap space used by
 * the popped element.
 */
Stack* pop(Stack *stack) {
    
    Stack* buffer;    //Create a buffer in memory to store the next stack node pointer

    if(isEmpty(stack) == TRUE) {
	printf("You cannot use an empty stack in the pop function.\n");
        return stack;
    } else {
	buffer = stack->next;
	free(stack);
	return buffer;
    }        
} // end pop

/*
 * This function returns the number of integers in a stack.
 */
int countInts(Stack *stack) {
    
    int iCounter = 0;     //counts the number of ints 
    if (isEmpty(stack) == TRUE) {    //return 0 if the stack has no ints
        return 0; 
    }
    Stack* nextNode = stack;

    do {
        if (nextNode->intTop == TRUE) {    //increase counter when an int is found
	    iCounter++;
        }
        nextNode = nextNode->next;
    } while (nextNode != NULL);    //loop until the next node is null
    return iCounter; 
} // end countInts

/*
 * This function returns the number of strings in a stack.
 */
int countStrings(Stack *stack) {
  
    int iCounter = 0;     //counts the number of ints 
    if (isEmpty(stack) == TRUE) {    //return 0 if the stack has no ints
        return 0; 
    }
    Stack* nextNode = stack;

    do {
        if (nextNode->intTop == FALSE) {    //increase counter when an int is found
	    iCounter++;
        }
        nextNode = nextNode->next;
    } while (nextNode != NULL);    //loop until the next node is null
    return iCounter; 
  
} // end countStrings

