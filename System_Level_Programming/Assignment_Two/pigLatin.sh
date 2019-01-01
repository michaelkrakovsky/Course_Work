#The following script will perform pig latin. The code was written by Michael Krakovsky. Student ID: 10134030

WORD=$1;     #Stores the parameter
FIRSTLETTER=${WORD:0:1} #stores the first letter   

if [[ "$#" -ne 1 ]];        #Ensure the number of parameters is one
then
    >&2 echo "wrong number of arguments for pigLatin.sh (needs exactly one)";
    exit 1;
fi

for i in $(seq 1 ${#WORD});    #Loop through the entire word
do 
    char=${WORD:$i:1};       #stores the character that is being compared
    for vowel in a e i o u;   #Check to see if it is a vowel
    do  
        if [[ "$vowel" == "$FIRSTLETTER" ]]; #Echo response if the vowel is the first letter
        then 
            echo "${WORD}way";
            exit 0;
        elif [[ "$vowel" == "$char" ]];            #Echo when the vowel is reached
        then
	    echo "${WORD:i}${WORD:0:i}ay";  
            exit 0;
        fi
    done
done

echo "${WORD}ay";   #If the word doesn't have vowels, add ay
