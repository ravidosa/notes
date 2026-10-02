#include "sorter.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/* This loads the specified file into a new loaded_file
 * structure.  In particular it breaks up each line (by '\n')
 * and loads it into a line_struct, storing it in the
 * newly allocated file struct.
 * 
 * It is OK to reallocate for each character and each line
 * (as realloc under
 * the hood won't actually move things except on a power-of-two
 * type boundary), but you need to read things in a character
 * at a time for this to work with binary data.
*/
loaded_file *load_file(FILE *f)
{
  (void) f;
  static loaded_file loaded_f;
  loaded_f.num_lines = 0;
  loaded_f.lines = calloc(1, __SIZEOF_POINTER__);

  line l;
  l.length = 0;
  l.data = calloc(1, 1);
  while (fread(l.data+l.length, 1, 1, f)) {
    l.length += 1;
    unsigned char *l_data = realloc(l.data, l.length + 1);
    if (!l_data) {
      return NULL;
    }
    else {
      l.data = l_data;
      if (l.data[l.length - 1] == '\n') {
        loaded_f.num_lines += 1;
        line **lf_lines = realloc(loaded_f.lines, loaded_f.num_lines * (__SIZEOF_POINTER__));
        if (!lf_lines) {
          return NULL;
        }
        else {
          loaded_f.lines = lf_lines;
          loaded_f.lines[loaded_f.num_lines - 1] = malloc(sizeof(l));
          memcpy(loaded_f.lines[loaded_f.num_lines - 1], &l, sizeof(l));
          loaded_f.lines[loaded_f.num_lines - 1]->length = l.length;
          l.length = 0;
          l.data = calloc(1, 1);
        }
      }
    }
  }
  free(l.data);
  return &loaded_f;
}

/*
*/
void free_file(loaded_file *f)
{
  if (f->num_lines) {
    for (size_t i = 0; i < (f->num_lines); i++) {
      if (f->lines) {
        if ((f->lines)[i]) {
          if ((f->lines)[i]->data) {
            free((f->lines)[i]->data);
            free((f->lines)[i]);
          }
        }
      }
    }
  }
  free(f->lines);
}

/*
 * the C qsort() utility takes a comparison function that
 * is a little different.  Becaues it wants to work on data that
 * can be of arbitrary sized (so, eg, an array of structures) rather
 * than just void* items, it wants pointers-to-pointers.
 * 
 * Similarly we can't use strcmp in this because we actually need
 * to evaluate strings that can contain null pointers.  But we will
 * just do strict character comparison:  
 * 
 * for i from 0 to length of min(a/b), if a[i] < b[i] then its -1,
 * if a[i] > b[i] its +1, and if a[i] = b[i] we increment i.
 * Then its the shorter string is before, and 0 if the
 * strings are fully equal.
*/
int sorter_comp(const void *a, const void *b){
  (void) a;
  (void) b;
  line la = **(line **)a;
  line lb = **(line **)b;
  size_t minlen = la.length;
  if (la.length > lb.length) {
    minlen = lb.length;
  }
  for (size_t i = 0; i < minlen - 1; i++) {
    if (la.data[i] < lb.data[i]) {
      return -1;
    }
    if (la.data[i] > lb.data[i]) {
      return 1;
    }
  }
  if (la.length < lb.length) {
    return -1;
  }
  else if (la.length > lb.length) {
    return 1;
  }
  return 0;
}

/* You probably want to use qsort */
void sort_file(loaded_file *f)
{
  (void) f;
  qsort(f->lines, f->num_lines, __SIZEOF_POINTER__, sorter_comp);
}

/*
 * As a reminder the lines can include nulls, so C printing of string
 * routines can't work.  Instead we need to print the string a character
 * at a time to standard output using putchar()
*/
void print_file(loaded_file *f)
{
  (void) f;
  for (size_t i = 0; i < f->num_lines; i++) {
    for (size_t j = 0; j < (f->lines)[i]->length; j++) {
      putchar(((f->lines)[i]->data)[j]);
    }
  }
}
