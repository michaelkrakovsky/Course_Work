/*
 * Headers for functions to be written by students for Assignment 4.
 * CISC 220, Fall 2017
 */

// Returns the number of space characters (' ') in its parameter
int countSpaces(char theString[]);

/*
 * Splits a string into individual words.  
 * First parameter: a string.  Assumes that the words in the string are separated by
 *   single spaces, with no spaces before the first word or after the second word.  So
 *   the number of words is equal to the number of spaces plus 1.  Punctuation will always
 *   appear at the end of a word and should be considered part of the word.
 * Second parameter: the address of an integer in which the function will store the
 *   number of words in the string.
 * Return value: pointer to the beginning of an array of strings containing the individual
 * words from the sentence.  This function creates that array and the strings inside the array,
 * using space from the heap for both the array and the individual words.  The strings are copies 
 * of words from the sentence, not pointers into the sentence. 
 */
char** splitString(char theString[], int *arraySize);

/* Cleans up the space used by an array of words.  
 * Parameters: array of words and its length
 * Assumes that the array of words and each individual word are stored on the heap.  
 * Frees the space used by the array AND each individual word.  Assumes that all 
 * words are null-terminated strings.
 */
void cleanup(char *words[], int numWords);
