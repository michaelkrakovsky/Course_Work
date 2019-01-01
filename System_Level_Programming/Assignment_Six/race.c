/*
 * The program accepts two parameters, which are executable programs.
 * The program executes both programs in parallel until one finishes.
 * The program reports the winner race.
 * 
 * The code was written by Michael Krakovsky.
 * Version 1.0
 * The code was written on December 3, 2017.
*/

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char** args) {

    if(argc != 3) {     //ensure there are exactly 2 parameters 
	printf("I am sorry, you have failed to enter 2 parameters.\n");
	exit(2);
    } else {
        args[3] = '\0';  //add a null character to the end of the array
    }
    pid_t childOne = fork();
    if(childOne < 0) {   //indicate error
	printf("*** Error: The process was unable to fork.\n");
	exit(1);
    } else if (childOne == 0) {   //execute first program unless error occurs
        if(execvp(args[1], args) == -1) {
            printf("%s could not be executed.", args[1]);
	    exit(2);
        }
    }
    pid_t childTwo = fork();
    if(childTwo < 0) { //indicate error
	printf("*** Error: The process was unable to fork.\n");
	exit(1);
    } else if (childTwo == 0) {    //execute second program
        if(execvp(args[2], args) == -1) {
            printf("%s could not be executed.", args[2]);
	    exit(2);
        }
    }
    int status;    //displays the exit status
    int waitResult;  //displays the address of the process

    while (1) {
        waitResult = wait(&status);  // wait to see which program finishes first, and what status they finished with
        if (waitResult == childOne) {
	    if (status != 0) {         //Indicates a bad program
	        printf("%s failed. %s is the winner.\n", args[1], args[2]); 
	    } else {
	        printf("The winner is %s.\n", args[1]);  
	    }
	kill(childTwo, SIGKILL);
        exit(EXIT_SUCCESS);     //kill the other fork child and exit successfully
	} else if (waitResult == childTwo) {
	    if (status != 0) {         //Indicates a bad program
	        printf("%s failed. %s is the winner.\n", args[2], args[1]); 
	    } else {
	        printf("The winner is %s.\n", args[2]);  
	    }
	kill(childOne, SIGKILL);
        exit(EXIT_SUCCESS);     //kill the other fork child and exit successfully
        } else {
	    printf("The program has failed to run.\n");
            exit(EXIT_FAILURE);
	}
    }
    return 0; 
}
