/* The following code was written by Michael Krakovsky. (10134030)
 * The code will allow the user to play a game of pig against the computer. The computer will continue to roll until it reaches 100 or more than 20.
 */

import javax.swing.JOptionPane;  //Import module to print windows to the screen 
import java.util.concurrent.ThreadLocalRandom; //Import the ability to create new random numbers 

public class Assn1_10134030 {    //Main class 
	
	public static int getRandomNumber (String whosRolling, String whichRoll) {     //method that returns a random integer between 1 and 6
		
		int randomNumber = ThreadLocalRandom.current().nextInt(1, 6 + 1); //Code taken from Stack Overflow stating how to create a random number within a given range (i.e. Number on a die)		   														      //return a random number between 1, 6	   
		
		System.out.println("The " +  whosRolling + " rolled a: " + randomNumber + " on roll " + whichRoll + ".");    // Show what the users first roll is 
		
		return randomNumber;  //return the value of the dice

	}	
	
	public static String readUserResponse (String userPrompt)   {    //method to reads the prompt and dictates further action     
        
	    if (userPrompt.equals("y") || userPrompt.equals("yes")) {           //return a simplified yes if the user indicates a yes
	    	return "yes";     
	    	
	    } else if (userPrompt.equals("n") || userPrompt.equals("no")) {        //return a simplified no if the user indicates no
	    	return "no";      
	    	
	    } else {
	    	JOptionPane.showMessageDialog(null, "Please enter yes or no.");       //return an invalid if no response makes sense
	    	return "invalid";   
	    }
	}
	
	public static String getUserPrompt () {    //The following method gets the prompt of the user
		
		String userPrompt = null; //variable to store the users prompt
		
		do {
	        userPrompt =  JOptionPane.showInputDialog("Do you wish to roll the dice? (y/n) ");    //Prompt the user to roll the dice
	    	userPrompt = userPrompt.toLowerCase();      //Transfer everything to lower case for lighter conditional statements
		    
		    userPrompt = readUserResponse(userPrompt);      //simplify the users response 
		    
	    } while (userPrompt == "invalid");  //keep prompting the user until their response is valid

	    return userPrompt;             
	}
	
	public static int turnTotal (int rollOne, int rollTwo) {        //Method that takes two arguments and returns how many points the user receives
		
		if (((rollOne == 1) && (rollTwo != 1)) || ((rollOne != 1) && (rollTwo == 1))) {   //If only one dice is one, the user gets no points
			return 0;
			
		} else if ((rollOne == 1) && (rollTwo == 1)) {      //If both the dice equal 1, the user gets 25 points
			return 25;
			
		} else if (rollOne == rollTwo) {           //If the dice match, the user gets double of the sum of the dice
			return (rollOne + rollTwo) * 2;
			
		} else {
		    return (rollOne + rollTwo);        //As a default, simply return the sum of the dice
		
		}
	}
	
	public static int humanSingleTurn () {    //Method that executes a users turn and returns the human's running total of that specific turn
		
		int userRollOne = 0;            //Create the variables to store the users roll
		int userRollTwo = 0;
		int runningTotal = 0; 
		String userPrompt = null;        //create a variable to store user prompt
		
		do {       				//Iterate through the loop once before deciding what to do
			userRollOne = getRandomNumber("user", "one");         //Get the value of roll one
			userPrompt = getUserPrompt();						 //get the users prompt
			
			if (userPrompt == "no") {           //Return the users score if they wish to cut their turn short
				return (userRollOne + runningTotal);
			}
			
			userRollTwo = getRandomNumber("user", "two");         //Get the value of roll two
			runningTotal = runningTotal + turnTotal(userRollOne, userRollTwo); //Add the dice total, the following if statement block will indicate what the user truly scores
			
			if (userRollOne == userRollTwo) {       //Force the user to roll again since the rolled a double; however, notify them and add to their running total
				JOptionPane.showMessageDialog(null, "You rolled a double; therefore, you must roll again. You have gained " + turnTotal(userRollOne, userRollTwo) + " from that last roll!");
				
			} else if (turnTotal(userRollOne, userRollTwo) == 0) {              //If their turn score is 0, return 0
				return 0;			
			
			} else {
				userPrompt = getUserPrompt();   //see if the user wishes to go again as a default
				
			}
			} while (userPrompt == "yes");      //end the turn when the player doesn't wish to play
		
		System.out.println("You have accumulated " + runningTotal + " this round.");      //indicate the amount of points the user accumulates
		return runningTotal;      //Return the running total since the user has decided to cut the loop	
	}
	
	public static int computerSingleTurn (int humansRunningTotal, int computersRunningTotal) {  //Method that controls the processes of the computer. The computer plays until they reach more than 20, 
																								
		int runningTotal = 0;      				//stores the running score the computer as received 
		int computerRollOne = 0;        //stores the computers rolls
		int computerRollTwo = 0;
	    
		do {    
			
			if (humansRunningTotal >= 100) {   //If the human's score is above or equal to 100, the computer does not get a turn
				return 0;
			
			}
			
			if ((computersRunningTotal + runningTotal) >= 100 && computerRollOne != computerRollTwo) {   //end the loop if the numbers are not the same and the score is 100 (force the computer to roll again if they get doubles
				return runningTotal;
			
			}
			computerRollOne = getRandomNumber("computer", "one");      //generate the number for the computers first roll
			
			if (((runningTotal + computerRollOne) > 20) || ((runningTotal + computerRollOne + computersRunningTotal) >= 100)) {  //end the computers turn if they rolled the appropriate amount of points in their turn or passed 100
				System.out.println("The computer accumulated " + (runningTotal + computerRollOne) + " this round.");      //print the computers round score
				return (runningTotal + computerRollOne); 	
				
			}
			computerRollTwo = getRandomNumber("computer", "two");                  //generate the computers second roll and calculate what the value would be
			runningTotal = runningTotal + turnTotal(computerRollOne, computerRollTwo);
				
			if(turnTotal(computerRollOne, computerRollTwo) == 0) {   //end the computers turn if it rolls a one 
				return 0;            
			}
			
		} while (runningTotal <= 20 || computerRollOne == computerRollTwo); 	    //Iterate if the computer's score is less than or equal to 20 or if the dice are the same value
		
		System.out.println("The computer accumulated " + runningTotal + " this round.");         //print the computers round score
		return runningTotal;       
	}
	
	public static String whoWon(int humansRunningTotal, int computersRunnungTotal) {       //find out who won the game 
		
		if (humansRunningTotal > computersRunnungTotal) {							//return a friendly message regardless who wins
			return "The humans wins! Way to go, I hope this brightens your day.";
			
		} else {
			return "The computer wins and you lose... But as Jay-Z said, that's life, winners and losers."; 
			
		}
	}
		
	public static void runTheGame () {    //method that maintains the running total of both users, it runs the game until one user hits 100 points
		
		int humansRunningTotal = 0;       //stores the running values of both players
		int computersRunnungTotal = 0; 
		
		do {       		//iterates the game until one of the players reaches a score 100
			
			humansRunningTotal = humansRunningTotal + humanSingleTurn();      //run the humans turn    (Humans will always go first in this case)
			JOptionPane.showMessageDialog(null, "Your running total is: " + humansRunningTotal);       //When the users turn ends, show there total amount of points
			
			computersRunnungTotal = computersRunnungTotal + computerSingleTurn(humansRunningTotal, computersRunnungTotal);    //gather computers amount of points 
			JOptionPane.showMessageDialog(null, "The computers running total is: " + computersRunnungTotal);       //When the computer turn ends, show there total amount of points

			
		} while ((humansRunningTotal < 100) && (computersRunnungTotal < 100));     //end the loop if one of the users goes over 100
		
		JOptionPane.showMessageDialog(null, whoWon(humansRunningTotal, computersRunnungTotal));
	}
	
	public static void main(String[] args) { 		// TODO Auto-generated method stub
		
		runTheGame(); //run the game to see who wins

	}
}








	
	  
