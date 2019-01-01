# A makefile for building the Assignment 5 program from its
# source files
# CISC 220, Fall 2017

OBJ = stack.o stackTest.o 
CC = gcc
CFLAGS = -Wall

stackTest: $(OBJ)
	gcc -o stackTest $(OBJ)

stackTest.o: stack.h

stack.o: stack.h

# "make cleanup" gets rid of all the files produced by the
# make rules above
cleanup:

	rm -f stack.o stackTest.o stackTest *~*
