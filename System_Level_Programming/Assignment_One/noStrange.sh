#The following code takes a directory as an argument, then scans the directory to remove certain files
#The following code was written by Michael Krakovsky. Student ID: 10134030

PATH=$1      #Retrieve the directory

cd ${PATH}        #Change the path to the directory indicated by the user


/bin/rm -i x*y* x*y *x*y *x*y* xy* *xy* *xy        #Here is every combination in which xy whould appear in sequential                                                  #order within a word. The -i was added to ensure the user doesn't
                                              #remove the wrong file 
