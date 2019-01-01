/*
 * This program provides a menu-driven interface for testing
 * the required functions for Assignment 5.  It starts with
 * an empty stack and lets the user decide what operations
 * to perform on that stack.  
 * 
 * Provided for use in Assignment 5
 * CISC 220, Fall 2017
 */

// The module provided with the assignment -- type definitions and
// "forward declarations" for all required functions
#include "stack.h"

// Library modules
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// the maximum size of a string for the stack
// (including the ending'\0')
#define MAX_STRING_LENGTH 11

// Displays either TRUE or FALSE to describe an integer.
// (In C, 0 is false and everything else is true.)
void displayBoolean(int bool) {
  if (bool)
    printf("TRUE");
  else
    printf("FALSE");
} // end displayBoolean


// Discards the remainder of the current input line
void skipLine() {
  char ch = ' ';
  scanf("%c", &ch);
  while (ch != '\n') {
    scanf("%c", &ch);
  }
} // end skipLine


// Asks the user to enter a string.
// Parameters:
//   1. a prompt
//   2. a string to hold the user's input
//   3. the maximum number of characters to read (including
//      space for the ending '\0')
// If the user enters more than the maximum number of
// characters, skips over all the extra characters until
// the end of the input line.
void getString(char *prompt, char *input) {
  printf("%s", prompt);
  char ch = ' ';
  int i;
  for (i = 0; i < MAX_STRING_LENGTH-1; i++) {
    scanf("%c", &ch);
    if (ch == '\n') {
      input[i] = '\0';
      return;
    }
    else {
      input[i] = ch;
    } // end if
  } // end for
  
  input[i] = '\0';

  // If input string was too long,discard remaining characters
  // until end of line
  if (ch != '\n') {
    printf("String is too long for stack; will be truncated\n");
    while (ch != '\n') {
      scanf("%c", &ch);
    } // end while
  } // end if
} // end getString


// Asks the user for an integer; returns their answer.
// If the input is not a legal integer prints an error
// message and tries again.
int getInteger(char *prompt) {
  printf("%s", prompt);
  
  int theInteger;
  int scanResult = scanf("%d", &theInteger);
  // throw away rest of input line
  int ch=' ';
  while (ch != '\n')
    ch = getchar();
  if (scanResult != 1) {
    fprintf(stderr, "Error reading user choice: not an integer\n");
    return getInteger(prompt); // try again
  }
  else {
    return theInteger;
  } // end if
} // end getInteger


// constants for all of the menu choices
#define EXIT_CHOICE 1
#define EMPTY_TEST_CHOICE 2
#define PUSH_INT_CHOICE 3
#define PUSH_STRING_CHOICE 4
#define POP_CHOICE 5
#define TOP_VALUE_CHOICE 6
#define TOP_TYPE_CHOICE 7
#define COUNT_STRINGS_CHOICE 8
#define COUNT_INTS_CHOICE 9


int main() {
  // Stack to use for testing, intially empty
  Stack *theStack = NULL;


  while (TRUE) {
    printf("Next test (1=exit, 2=isEmpty, 3=pushInt, ");
    printf("4=pushString, 5=pop, 6=top value, \n");
    printf("           7=top type, 8=count strings, ");
    printf("9=count ints): ");
    
    int choice;
    choice = getInteger("");

    if (choice == EXIT_CHOICE) {
      printf("DONE TESTING -- GOODBYE!\n");
      exit(0);
    }

    else if (choice == EMPTY_TEST_CHOICE) {
      int emptyResult = isEmpty(theStack);
      printf("Result of isEmpty: ");
      displayBoolean(emptyResult);
      printf("\n");
    }

    else if (choice == PUSH_INT_CHOICE) {
      int pushValue = getInteger("value to push onto stack: ");
      theStack = pushInt(theStack, pushValue);
    }

    else if (choice == PUSH_STRING_CHOICE) {
      char pushValue[MAX_STRING_LENGTH];
      getString("value to push: ", pushValue);
      theStack = pushString(theStack, pushValue);
    }

    else if (choice == POP_CHOICE) {
      theStack = pop(theStack);
    }

    else if (choice == TOP_VALUE_CHOICE) {
      if (isEmpty(theStack))
	printf("there is no top value\n");
      else if (topIsInt(theStack))
	printf("the top value is %d\n", topInt(theStack));
      else { // top element must be a string
	char tempString[MAX_STRING_LENGTH];
	topString(theStack, tempString);
	printf("the top value is \"%s\"\n", tempString);
      }
    }

    else if (choice == TOP_TYPE_CHOICE) {
      if (isEmpty(theStack))
	printf("Nothing on top of an empty stack\n");
      else if (topIsInt(theStack))
	printf("Integer on top\n");
      else
	printf("String on top\n");
    }

    else if (choice == COUNT_INTS_CHOICE) {
      printf("%d integer(s) on the stack\n", countInts(theStack));
    }

    else if (choice == COUNT_STRINGS_CHOICE) {
      printf("%d string(s) on the stack\n", countStrings(theStack));
    }

    else {
      fprintf(stderr, "ERROR: unknown menu choice\n");
    }
    
    printf("Stack is: "); printStack(theStack);
    printf("\n");
  } // end while
  
    exit(0);
} // end main
