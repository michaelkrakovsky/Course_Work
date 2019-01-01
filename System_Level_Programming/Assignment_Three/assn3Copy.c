#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*The c file will be used for grade analytics. The full description for the functionality of the 
program can be located within the assignment description. 
Author: Michael Krakovsky (Student: 10134030)
Version: 1.0
*/

/*create define variables that include: the amount of grades you can enter, 
the max grade value allowed, the min grade value allowed, the exit value*/
#define ARRAYSIZE 20 
#define MAXVALUEALLOWED 100
#define MINVALUEALLOWED -1
#define EXITVALUE -1

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

/*A function that iterates through the entire array and retuns the max value
The function require two parameters: an array with grades, the number of grades within the array*/
int findMax(int gradeArray[], int numberOfInputs) {
    
    int maxValue = gradeArray[0];      /*Stores the max value of the array*/
    
    for(int i = 0; i < numberOfInputs; i = i + 1) {    /*Iterate through the array and find the max value*/
        if(gradeArray[i] > maxValue) {
            maxValue = gradeArray[i];
        } 
    }
    return maxValue;
}

/*A function similar to the one on top but returns a min value
The functions require two parameters: an array with grades, the number of grades within the array*/
int findMin(int gradeArray[], int numberOfInputs) {
    
    int minValue = gradeArray[0];      /*Stores the max value of the array*/
    
    for(int i = 0; i < numberOfInputs; i = i + 1) {    /*Iterate through the array and find the max value*/
        if(gradeArray[i] < minValue) {
            minValue = gradeArray[i];
        } 
    }
    return minValue;
}    
/*The function will provide the average of the grades
The functions require two parameters: an array with grades, the number of grades within the array*/ 
float findAverage(int gradeArray[], int numberOfInputs) {

    float sum = 0.0f;
    
    for(int i = 0; i < numberOfInputs; i = i + 1) {
        sum = sum + gradeArray[i];
    }
    return (sum / numberOfInputs);
}
/*The function will return the standard deviation of the inputs.
The functions require two parameters: an array with grades, the number of grades, and the average*/ 
double findStdDeviation(int gradeArray[], int numberOfInputs, double average) {
    
    float differencesSquared[numberOfInputs];
    float differencesSquaredSum = 0.0f; 
    double root;

    for(int i = 0; i < numberOfInputs; i = i + 1) {  //square the differences of the average and add together
        differencesSquared[i] = gradeArray[i] - average;
        differencesSquared[i] = differencesSquared[i] * differencesSquared[i]; 
        differencesSquaredSum = differencesSquaredSum + differencesSquared[i];   
    }
    root = (differencesSquaredSum / numberOfInputs);
    root = sqrt(root);
    return root;
}

/*Function that prints the number of As, Bs, Cs, Ds, and Fs
The function requires the grades array and the number of grades enterd*/ 
void divideGrades(int gradeArray[], int gradeBin[], int numberOfGrades) {

    for(int i = 0; i < numberOfGrades; i = i + 1) { //Decide the corresponding letter grade for each value
        if(gradeArray[i] < 50) {
            gradeBin[0] = gradeBin[0] + 1;
        } else if((gradeArray[i] >= 50) && (gradeArray[i] <= 59)) {
            gradeBin[1] = gradeBin[1] + 1;
        } else if((gradeArray[i] >= 60) && (gradeArray[i] <= 69)) {        
            gradeBin[2] = gradeBin[2] + 1;
        } else if((gradeArray[i] >= 70) && (gradeArray[i] <= 79)) {        
            gradeBin[3] = gradeBin[3] + 1;
        } else {
            gradeBin[4] = gradeBin[4] + 1;
        }
    }
    //Print the results to the screen
    printf("The number of As: %d \n", gradeBin[4]);
    printf("The number of Bs: %d \n", gradeBin[3]);
    printf("The number of Cs: %d \n", gradeBin[2]);
    printf("The number of Ds: %d \n", gradeBin[1]);
    printf("The number of Fs: %d \n", gradeBin[0]);
}

/*Function makes a report containing the min value, max value, the average mark, and the standard deviation
The parameters include the array with the grades, and the number of inputs within the array*/
void createReport(int maxValue, int minValue, float average, double stdDeviation, int numberOfGrades) {
    
    printf("You have inputed %d grade(s).\n", numberOfGrades); //print value
    printf("The minimum value is: %d \n", minValue);
    printf("The maximum value is: %d \n", maxValue);   
    printf("The average is: %.2f \n", average);
    printf("The standard deviation: %.2f \n \n", stdDeviation);
}

//Main function ties everything together
int main(void) {
    
    int * storeGradesPointer;  /*Store grades to an array and assign a pointer to the array*/
    int storeGradesArray[ARRAYSIZE];
    storeGradesPointer = storeGradesArray;

    int numberOfGrades = getUserInput(storeGradesPointer); //Store the number of inputs from the user
    int maxValue = findMax(storeGradesPointer, numberOfGrades); //Find the maximum value
    int minValue = findMin(storeGradesPointer, numberOfGrades);   //find the min value
    float average = findAverage(storeGradesPointer, numberOfGrades); //find the average
    double standardDeviation = findStdDeviation(storeGradesPointer, numberOfGrades, average); 
    //find the standard deviation
    
    int * defineGradesPointer;      //Create an array to manipulate
    int defineGradesArray[5] = {0, 0, 0, 0, 0};
    defineGradesPointer = defineGradesArray;

    createReport(maxValue, minValue, average, standardDeviation, numberOfGrades);    
    divideGrades(storeGradesPointer, defineGradesPointer, numberOfGrades);
    return 0;
}



 
