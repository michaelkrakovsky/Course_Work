/*
 * A function that will print a message telling you how much heap space 
 * you're using. 
 * Provided for use in Assignment 4.
 * Don't worry if you don't understand how it works; we haven't 
 * discussed structs yet!
 * CISC 220, Fall 2016
 * M. Lamb
 */
#include <malloc.h>
#include "heapReport.h"

/* Writes a line to the standard output, reporting your program's
 * current heap use.  
 */
void heapReport() {

  /* The mallinfo function (from library malloc.h) returns a struct
   * describing various aspect of the heap */
  struct mallinfo heapInfo = mallinfo();

  /* the uordblks element of the struct contains the number we want:
   * the number of bytes in currently allocated heap areas */
  printf("heap use %d\n", heapInfo.uordblks);
} // end heapReport 
