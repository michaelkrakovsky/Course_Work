#include <stdio.h>
#include <stdlib.h>
#include "readMarks.h"

/*create define variables that include: the amount of grades you can enter, 
the max grade value allowed, the min grade value allowed, the exit value*/
#define ARRAYSIZE 20 
#define MAXVALUEALLOWED 100
#define MINVALUEALLOWED -1
#define EXITVALUE -1

//Read marks from the user
/*The function will ask for user input, 
store the grades in array declared in main, 
and return the number of inpus by the user*/
int getUserInput(int storeGrades[]) {
    
    int userInput;    /*Stores user input*/
    int numberOfInputs = 0;   /*Stores the number of times the user enters a number*/
     
    while (numberOfInputs < ARRAYSIZE) {    /*Loop for a maximum of 20 times*/
        printf("Please enter a grade or -1 to exit.  The number must be within 0 and 100. (inclusive): ");
        if (scanf("%d", &userInput) != 1) {    /*Check to see if the input is legal*/ 
            printf("ERROR: You have entered a non-integer value.\n");             
            exit(3); /*Exit the program with a non-zero value*/
        } else if ((userInput == EXITVALUE) && (numberOfInputs == 0)) {
            printf("ERROR: You exited the program before entering a grade.\n");
            exit(2); /*Exit with a non-zero value*/
        } else if (userInput == EXITVALUE) {
            printf("You have indicated that you wanted to exit by entering -1.\n");
            return numberOfInputs;
        } else if ((userInput < MINVALUEALLOWED) || (userInput > MAXVALUEALLOWED)) {
            printf("This is not a legal value. Please enter a value between 0 - 100.\n");
        } else {
            storeGrades[numberOfInputs] = userInput;     /*Add the variable to the array and increase the counter*/
            numberOfInputs = numberOfInputs + 1;
        }
        if (numberOfInputs == ARRAYSIZE) {      /*Indicate to the user that they reached the amount of values they could enter*/
            printf("You have entered the maximum amount of values allowed.\n");
        }
    }
    return numberOfInputs; 
}
