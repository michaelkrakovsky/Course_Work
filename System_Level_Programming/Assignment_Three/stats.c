#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "stats.h"

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


