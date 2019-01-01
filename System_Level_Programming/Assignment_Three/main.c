#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "stats.h"
#include "readMarks.h"
#include "main.h"

/*create define variables that include: the amount of grades you can enter, 
the max grade value allowed, the min grade value allowed, the exit value*/
#define ARRAYSIZE 20 
#define MAXVALUEALLOWED 100
#define MINVALUEALLOWED -1
#define EXITVALUE -1

//Main part of the function
int main () {
    
    int * storeGradesPointer;  /*Store grades to an array and assign a pointer to the array*/
    int storeGradesArray[ARRAYSIZE];
    storeGradesPointer = storeGradesArray;
    
    int numberOfGrades = getUserInput(storeGradesPointer); //Store the number of inputs from t
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
