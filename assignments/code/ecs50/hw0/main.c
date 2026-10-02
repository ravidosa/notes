#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "sorter.h"

/* This simple main should work as follows:
   For each filename passed as a command line argument:
   
   1)  Open the file.  If the file fails to open, exit with code 42
   2)  Load the file into a loaded_file structure using load_file
   3)  When the file is loaded, sort the file with sort_file
   4)  When the file is sorted, print the file to standard output with
       print_file
   5)  Free the loaded_file structure with free_file, and close
       the FILE pointer itself

   If there are no files specified it should simply exit.
*/

int main(int argc, char **argv) {
  (void) argc;
  (void) argv;

  FILE* f_pointer;
  loaded_file* lf_ptr;

  for (int i = 1; i < argc; i++) {
    f_pointer = fopen(argv[i], "rb");
    if (f_pointer == NULL) {
      return 42;
    }
    else {
      lf_ptr = load_file(f_pointer);
      if (lf_ptr) {
        sort_file(lf_ptr);
        print_file(lf_ptr);
        free_file(lf_ptr);
      }
      fclose(f_pointer);
    }
  }
  return 0;
}
