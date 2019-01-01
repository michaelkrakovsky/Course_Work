#The following script was written by Michael Krakovsky. (Student ID: 10134030)
#The script will mark assignments

MARKINGSCRIPT=$1;    #Two variables that store the marking script and the folder containing the files
SUBMISSIONS=$2;
declare -ia MARKDIST=(0 0 0 0 0);       #Array that stores the grades distribution
GRADE="";                      #Stores the grade of the file

if [[ "$#" -ne 2 ]];    #Ensure the number of arguments is equal to two
then
    >&2 echo "The number of parameters does not match two.";
    exit 1;
fi

if ! [[ -d "$2" ]];         #Check to see if the second argument is correct
then 
    >&2 echo "$SUBMISSIONS is not an existing directory.";
    exit 2;
fi

if ! [[ -f "$1" ]] || ! [[ -x "$1" ]];        #Check to see if the first argument is correct  
then
    >&2 echo "$MARKINGSCRIPT is not an executable, existing file.";
    exit 2;
fi

for FILE in $SUBMISSIONS/*;      #Loop through every file within the submissions directory
do 
    GRADE=$($MARKINGSCRIPT $FILE);        #Store the grade of the submission    
    if [[ $GRADE == "A" ]];            #If statements that keep track of the grades
    then
        let MARKDIST[0]++;
    elif [[ $GRADE == "B" ]];
    then
        let MARKDIST[1]++;
    elif [[ $GRADE == "C" ]];
    then
        let MARKDIST[2]++;
    elif [[ $GRADE == "D" ]];
    then
        let MARKDIST[3]++;
    else
        let MARKDIST[4]++;
    fi
done

echo "A: ${MARKDIST[0]}";       #Print the letter grades to the screen 
echo "B: ${MARKDIST[1]}";
echo "C: ${MARKDIST[2]}";
echo "D: ${MARKDIST[3]}";
echo "F: ${MARKDIST[4]}";

exit 0;    #Exit as a 0 status to indicate a perfect run
