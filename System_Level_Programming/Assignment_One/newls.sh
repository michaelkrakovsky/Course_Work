#Script 1 --> Varrying the ls command
#The following code is written by Michael Krakovsky: Student ID 10134030

PATH=$1               #Take the path from the user

cd ${PATH}            #Change the path to what the user desires 

                    
/bin/ls -g -S -r -Q ${PATH}  #Command -g lists the files in the long format but does not include the owner 
                      #name of the files. The added -S sorts the filenames based on file size
		      #The -r reverses the sorting order so the files will increase in increasing order
		      #The added Q adds quotes to the file name as suggested by the question
		 






