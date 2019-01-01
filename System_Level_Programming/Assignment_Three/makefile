# Make file for Assignment 4
# Provided to help you compile and link your program
# CISC 220, Fall 2017

# flags for the automatic compilation rules:
# 1. use the GNU C compiler
CC=gcc
# 2. enable helpful warnings
CFLAGS=-Wall

assn3: main.o readMarks.o stats.o
	gcc -o assn3 main.o readMarks.o stats.o -lm
#main.o: main.c main.h 
readMarks.o: readMarks.c readMarks.h
stats.o: stats.c stats.h

# "make cleanup" will get rid of all non-source files.
cleanup:
	rm -f main.o readGrades.o stats.o assn3
