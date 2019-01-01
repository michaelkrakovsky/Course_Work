/*
 * This module contains a main function that you can use for 
 * testing your solution for Assignment 4.  Please don't waste 
 * server space by handing it in.  We will use a slightly different 
 * testing module, to make sure your funtions aren't specifically 
 * tailored to these test cases.  Feel free to write additional 
 * testing of your own as well.
 * 
 * CISC 220, Fall 2016
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// heapReport.h contains a header for a heapReport function which 
// tells you how much heap space your program is currently using
#include "heapReport.h"
// assn4Functions.h contains headers for the functions to be written by
// students for Assigment 4
#include "assn4Functions.h"


/*
 * Displays an array of words as returned by splitString.
 * The words have quotation marks around them so that it will be 
 * easy to see if the words contain spaces at the beginning
 * or end (which they shouldn't!).
 */
void displayWords(char *wordArray[], int numWords) {
  // The enclosing if statement is here so that when the program is
  // run with the stub version of splitString this function will
  // do nothing instead of crashing with a null pointer.
  // Students don't need to change this function.
  if (wordArray != NULL) {
    int i;
    for (i = 0; i < numWords; i++)
      printf("%i. \"%s\"\n", i+1, wordArray[i]);
  } // end for
} // end displayWords


int main() {
  printf("TESTING countSpaces:--------------\n");
  printf("should be 3: %d\n", countSpaces("one two three four")); 
  printf("should be 11: %d\n", countSpaces("  a     b   c ")); // should print 11
  printf("should be 0: %d\n", countSpaces("singleword")); // should print 0
  printf("----------------------------------\n");

  printf("Before any calls to malloc: ");  heapReport();

  #define NUM_SENTENCES 5  
  char *hamlet[] = {"Give every man thy ear, but few thy voice.",
		    "Neither a borrower nor a lender be.",
		    "For loan oft loses both itself and friend",
		    "And borrowing dulls the edge of husbandry.",
		    "This above all: to thine own self be true."};
  int i;
  for (i = 0; i < NUM_SENTENCES; i++) {
    int size;
    char **words = splitString(hamlet[i], &size);
    displayWords(words, size);
    printf("before cleaning up space for this sentence: "); heapReport();
    cleanup(words, size);
    printf("after cleaning up space: "); heapReport();
    printf("\n");
  }

  printf("end of program: "); heapReport();

  return 0;
} // end main
