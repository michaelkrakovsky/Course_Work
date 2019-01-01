# Make file for Assignment 4
# Provided to help you compile and link your program
# CISC 220, Fall 2017

# flags for the automatic compilation rules:
# 1. use the GNU C compiler
CC=gcc
# 2. enable helpful warnings
CFLAGS=-Wall

assn4: heapReport.o assn4Testing.o assn4Functions.o; gcc -o assn4 assn4Testing.o heapReport.o assn4Functions.o 
heapReport.o: heapReport.c heapReport.h
assn4Testing.o: assn4Testing.c
assn4Functions.o: assn4Functions.c assn4Functions.h

# "make cleanup" will get rid of all non-source files.
cleanup:
	rm -f heapReport.o assn4Testing.o assn4Functions.o assn4
