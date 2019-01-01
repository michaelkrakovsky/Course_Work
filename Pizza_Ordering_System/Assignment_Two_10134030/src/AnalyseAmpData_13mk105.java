/*The following program was written by Michael Krakovsky. Student ID: 10134030.
  The purpose of the code is to read in a csv file and produce a text file regarding
  the health of the motors.
*/

import java.io.File;                 //import classes to read in csv file and to write csv files
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import java.io.PrintWriter;

public class AnalyseAmpData_13mk105 {
	
	public static String[] csvFile () {                //Method that reads the csv file and returns everything in strings. I prefer to read the data set in first
													  //then I will do the parsing in a separate method to make my functions a bit more manageable 
		String[] dataSet = new String[1000];    
		String fileName = "bin/Logger.csv";    //adding bin ensure java looks within the src file to retrieve the filename
		File file = new File(fileName);      //object from java import file that reads in files
		int iCounter = 0; //counter that runs through entire string array
        
		try {
            Scanner input = new Scanner(file);	   //allows the file to be read  
         
            while (input.hasNext()) {     //while loops line by line
            	dataSet[iCounter] = input.nextLine();   //input the data into the string array
            	iCounter++;  //increase counter 
            }
            input.close(); //close the scanner 
		} catch (FileNotFoundException e) {      //catch the exception that the file does not exists
			System.out.println("Your file cannot be found.");
            System.exit(0); //end the program
		}
		return dataSet;  //return the data file to be processed
	}
  
	public static double[][] parseFile (String[] csvFile) {         //Method that further parses the data into a two dimensional array. (8 rows and 1000 columns)
		
        double[][] dataFile = new double[1000][7];    //stores all the data
        String[] temporaryStorage = new String[8];    //stores parsed data to be converted to a double
        
        for (int i = 0; i < 1000; i++) {   //we can assume that the data file only has 1000 entry all the time  
        	temporaryStorage = csvFile[i].split(",");     //Parse the string to be converted and inserted
        	for (int j = 0; j < 7; j++) {
			    dataFile[i][j] = Double.parseDouble(temporaryStorage[j + 1]);    //converts strings into a double and stores it 
        	}
        }
        return dataFile;  //return the fully parsed data
	}
	
	public static int runningTime (int iterationNumber, double[][] parsedFile, int motorNumber) {              //Method that stores the running time when the motor flips on 
		
		int totalRunningTime = 0;             //tracks the total running time
	
		while (parsedFile[iterationNumber + 1][motorNumber] > 0.01) {		
			totalRunningTime++;     //increase the total running time if the next number is above 0.01
			iterationNumber++;      //move the counter up one
		}
	    return totalRunningTime;                 //return the running time of the motor
	}
	
	public static void writeTextFile (int motorNumber, int endTime, int startTime, double averageTime, boolean exceededEight) {   //Method that writes the analytic information within a csv file
		
		try {              //we need to use a try catch to ensure that the file exists and it is not corrupt
		    File analyticText = new File("Motor" + (motorNumber + 1) + ".csv");
		        if (analyticText.exists() == false)      {         //checks if the file exists or not
		        	analyticText.createNewFile();   //create file if it doesn't exists
		        	PrintWriter writeText = new PrintWriter(analyticText);       //write the appropriate text within the file (title information)  
		        	if (endTime == 0 && startTime == 0 && averageTime == 0) {    //if the machine didn't run, indicate it	
			 		    writeText.println("The motor was not used.");
					    writeText.close();  
		        	} else {           //title text within the csv file
		        		writeText.println("start (sec), finish (sec), current (amps)");
					    writeText.close();
		        	}
		        }
		    if (endTime != 0 && startTime != 0 && averageTime != 0) {    //if the machine ran, write the appropriate text within the file 
		    	PrintWriter writeText = new PrintWriter(new FileWriter(analyticText, true));         
			    writeText.println(startTime + ", " + endTime + ", " + averageTime);
			    if (exceededEight == true) {       //indicate that the current surge exceeded over 8 amps    
			        writeText.println("***Previous Current Exceeded 8.0***");				
			    }
			     writeText.close();    
		    }		    
			} catch (IOException e) {
				e.printStackTrace();    //catch exception and display error
			}  
	}

	public static void runningAnalytics (double[][] motorFile, int iterationNumber, int motorNumber, int runningTime) {     //Method that states the start time, end time, and average of the pulse
		
	    double sumOfAmps = 0.0D;    //stores the sum of the pulses
	    boolean exceededEight = false;     //flags whether current exceeded of 8 amps
	    
	    for (int i = iterationNumber; i <= (iterationNumber + runningTime); i++) {     //for loop that captures the data specifically the time the motor ran
	    	if (motorFile[i][motorNumber] > 8.0D) {     //raise the flag if the amp exceeds 8	
	    		exceededEight = true;
	    	}
	    	sumOfAmps = sumOfAmps +  motorFile[i][motorNumber];       //adds to the running total
	    }
        //Quick Note: I needed to add a one two running time because it cover the start
	    if (exceededEight == true) {  //print the message in the text file
	    	writeTextFile(motorNumber, (iterationNumber + runningTime), iterationNumber, Math.round((sumOfAmps / (runningTime + 1)) * 1000D) / 1000D, true);    //run the text to draw the text file
	    } else {
	    	writeTextFile(motorNumber, (iterationNumber + runningTime), iterationNumber, Math.round((sumOfAmps / (runningTime + 1)) * 1000D) / 1000D, false);    
	    }
	}
	
	public static void isMotorRunning (int motorNumber) {         //Method that takes the parsed file and returns the analytical component of the task
		
		boolean isRunning = false;     //boolean that documents whether the machine is currently running
		double[][] parsedFile = parseFile(csvFile());     //parse the file and analyze
		motorNumber--;                  //since the array starts at 0, we need to take one off 
		
		for (int i = 0; i < 1000; i++) {        //loop through the entire file
			if (parsedFile[i][motorNumber] > 0.1D) {       //assume the machine is considered running when it exceeds 0.01 amps		
				runningAnalytics(parsedFile, i, motorNumber, runningTime(i, parsedFile, motorNumber));     //find the running time after the initial pulse occurs and run the analytics function
				i = i + runningTime(i, parsedFile, motorNumber);    //this moves the counter forward to skip over when the machine runs
				isRunning = true;    //assume the machine turned off
			}
		}
		if (isRunning == false) {      //if the machine hasn't run create the appropriate text file
			writeTextFile(motorNumber, 0, 0, 0, false);    //this will indicate to the function that the machine didn't run 
		}
	}
	
	public static void produceFiles () {  //Method that analyzes each motor
		
		for (int i = 1; i < 8; i++) {	
			isMotorRunning(i);
		}
	}
	
	public static void main(String[] args) {
			
		produceFiles();
		}
}
