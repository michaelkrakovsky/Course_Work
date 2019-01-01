/* File that contains the three functions. The funstion will allocate all of the 
* words from each sentence on the heap.
* Created by: Michael Krakovsky 
* Student ID: 10134030
* Version 1.0
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>

//Returns the number of space characters i.e (' ')

int countSpaces(char theString[]) {
    
    int length = strlen(theString);  //the index of the loop
    int numberOfSpaces = 0;    //assume it is already one (one for the last word)
	
    for (int i = 0; i < length; i++) {    //loop through the entire string
        if (theString[i] == ' ') { //if it is a space, count it
            numberOfSpaces++; 
        }
    }
    return numberOfSpaces;
}

//splits string into different words, separated by spaces
char** splitString(char theString[], int *arraySize) {
    
    char **containsStrings;
    containsStrings = malloc(strlen(theString) * sizeof(char*));  //new array to contain pointers    
    int newWord = 0;   //index for a new word 
    int lettersUntilSpace = 0;      //controls how big your individual string will be (remember to include an additional character for null
    int counter = 0;    //controls the while loop    
  
    if (!containsStrings) {   //ensure the array is not a null pointer
        exit(1);
    }
    //start parsing through the string and find the amount of charcters prior to the space
    while(counter < strlen(theString)) {
       while((theString[lettersUntilSpace + counter] != ' ') && (theString[lettersUntilSpace + counter] != '\n')) {
            lettersUntilSpace++;
	} 
        containsStrings[newWord] = malloc((lettersUntilSpace + 1) * sizeof(char));  //need to include an additional space for the char character
        for(int i = 0; i < lettersUntilSpace; i++) {	   
            containsStrings[newWord][i] = theString[counter + i];     //copy the character to the new string
            if(i == (lettersUntilSpace - 1)) {      
                containsStrings[newWord][i + 1] = '\0';       //add a null character 
            }
	}
        newWord++;
        counter = counter + lettersUntilSpace + 1;
        lettersUntilSpace = 0; //reset the value back to 0
    }
    *arraySize = newWord;
    return containsStrings;
}

//Cleans up the space use in the prevois function
void cleanup(char *words[], int numWords) { 

    for (int i = 0; i < numWords; i++) {
        free(words[i]);    //clear each space in memory
    }
    free(words);
}


