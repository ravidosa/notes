/*
 * Standard IO and file routines.
 */

/*
 * You MUST NOT add in any additional #includes below, the autograder will check!
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>
#include <string.h>
#include "floating.h"

/* This function is designed to provide information about
   the IEEE floating point value passed in.  Note that this
   ONLY works on systems where sizeof(float) == 4.

   For a normal floating point number it it should have a + or -
   depending on the sign bit, then the significand in binary in the
   format of the most significant bit, a decimal point, and then the
   remaining 23 bits, a space, and then the exponent as 2^ and then a
   signed integer.  As an example, the floating point number .5 is
   represented as "+1.00000000000000000000000 2^-1" (without the
   quotation marks).

   There are a couple of special cases: 0 should be "+0" or "-0"
   depending on the sign.  An infinity should be "+INF" or "-INF", and
   a NAN should be "NaN".

   For denormalized numbers, write them with a leading 0. and then the
   bits in the denormalized value.

   It should be safe: The output should be truncated if the buffer is
   not sufficient to include all the data.
*/
char *floating_info(union floating f, char *buf, size_t buflen)
{
  (void) f;
  for (int i = 0; i < buflen; i++) {
    buf[i] = 0;
  }
  size_t bufpos = 0;
  int exp = ((f.as_int >> 23) & 0xFF);
  int sign = ((f.as_int >> 31) & 0x1);
  int fraction = f.as_int & 0x7FFFFF;

  if (exp == 255) {
    if (fraction == 0) {
      if (bufpos < buflen - 1) {
        buf[bufpos] = (sign == 0 ? '+' : '-');
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 'I';
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 'N';
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 'F';
        bufpos++;
      }
    }
    else {
      if (bufpos < buflen - 1) {
        buf[bufpos] = 'N';
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 'a';
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 'N';
        bufpos++;
      }
    }
  }
  else if (exp == 0) {
    if (bufpos < buflen - 1) {
      buf[bufpos] = (sign == 0 ? '+' : '-');
      bufpos++;
    }
    if (bufpos < buflen - 1) {
      buf[bufpos] = 48;
      bufpos++;
    }
    if (fraction != 0) {
      if (bufpos < buflen - 1) {
        buf[bufpos] = '.';
        bufpos++;
      } 
      int bit = 0;
      while (bit < 23 && bufpos < buflen - 1) {
        buf[bufpos] = ((fraction >> (22 - bit)) & 0x1) + 48;
        bit++;
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 32;
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 50;
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 94;
        bufpos++;
      }
      exp -= 127;
      if (exp < 0 && bufpos < buflen - 1) {
        buf[bufpos] = 45;
        bufpos++;
      }
      exp = abs(exp);
      int dig = (exp >= 100 ? 3 : (exp >= 10 ? 2 : 1));
      while (dig > 0 && bufpos < buflen - 1) {
        buf[bufpos] = (exp / (dig == 3 ? 100 : (dig == 2 ? 10 : 1))) % 10 + 48;
        dig--;
        bufpos++;
      }
    }
  }
  else {
    if (bufpos < buflen - 1) {
      buf[bufpos] = (sign == 0 ? '+' : '-');
      bufpos++;
    }
    if (bufpos < buflen - 1) {
      buf[bufpos] = 49;
      bufpos++;
    }
    if (bufpos < buflen - 1) {
      buf[bufpos] = '.';
      bufpos++;
    } 
    int bit = 0;
    while (bit < 23 && bufpos < buflen - 1) {
      buf[bufpos] = ((fraction >> (22 - bit)) & 0x1) + 48;
      bit++;
      bufpos++;
    }
    if (bufpos < buflen - 1) {
      buf[bufpos] = 32;
      bufpos++;
    }
    if (bufpos < buflen - 1) {
      buf[bufpos] = 50;
      bufpos++;
    }
    if (bufpos < buflen - 1) {
      buf[bufpos] = 94;
      bufpos++;
    }
    exp -= 127;
    if (exp < 0 && bufpos < buflen - 1) {
      buf[bufpos] = 45;
      bufpos++;
    }
    exp = abs(exp);
    int dig = (exp >= 100 ? 3 : (exp >= 10 ? 2 : 1));
    while (dig > 0 && bufpos < buflen - 1) {
      buf[bufpos] = (exp / (dig == 3 ? 100 : (dig == 2 ? 10 : 1))) % 10 + 48;
      dig--;
      bufpos++;
    }
  }
  return buf;
}

/* This function is designed to provide information about
   the 16b IEEE floating point value passed in with the same exact format.  */
char *ieee_16_info(uint16_t f, char *buf, size_t buflen)
{
  (void) f;
  for (int i = 0; i < buflen; i++) {
    buf[i] = 0;
  }
  size_t bufpos = 0;
  int exp = ((f >> 10) & 0xFF);
  int sign = ((f >> 15) & 0x1);
  int fraction = f & 0x3FF;

  if (exp == 31) {
    if (fraction == 0) {
      if (bufpos < buflen - 1) {
        buf[bufpos] = (sign == 0 ? '+' : '-');
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 'I';
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 'N';
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 'F';
        bufpos++;
      }
    }
    else {
      if (bufpos < buflen - 1) {
        buf[bufpos] = 'N';
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 'a';
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 'N';
        bufpos++;
      }
    }
  }
  else if (exp == 0) {
    if (bufpos < buflen - 1) {
      buf[bufpos] = (sign == 0 ? '+' : '-');
      bufpos++;
    }
    if (bufpos < buflen - 1) {
      buf[bufpos] = 48;
      bufpos++;
    }
    if (fraction != 0) {
      if (bufpos < buflen - 1) {
        buf[bufpos] = '.';
        bufpos++;
      } 
      int bit = 0;
      while (bit < 10 && bufpos < buflen - 1) {
        buf[bufpos] = ((fraction >> (9 - bit)) & 0x1) + 48;
        bit++;
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 32;
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 50;
        bufpos++;
      }
      if (bufpos < buflen - 1) {
        buf[bufpos] = 94;
        bufpos++;
      }
      exp -= 15;
      if (exp < 0 && bufpos < buflen - 1) {
        buf[bufpos] = 45;
        bufpos++;
      }
      exp = abs(exp);
      int dig = (exp >= 10 ? 2 : 1);
      while (dig > 0 && bufpos < buflen - 1) {
        buf[bufpos] = (exp / (dig == 3 ? 100 : (dig == 2 ? 10 : 1))) % 10 + 48;
        dig--;
        bufpos++;
      }
    }
  }
  else {
    if (bufpos < buflen - 1) {
      buf[bufpos] = (sign == 0 ? '+' : '-');
      bufpos++;
    }
    if (bufpos < buflen - 1) {
      buf[bufpos] = 49;
      bufpos++;
    }
    if (bufpos < buflen - 1) {
      buf[bufpos] = '.';
      bufpos++;
    } 
    int bit = 0;
    while (bit < 10 && bufpos < buflen - 1) {
      buf[bufpos] = ((fraction >> (9 - bit)) & 0x1) + 48;
      bit++;
      bufpos++;
    }
    if (bufpos < buflen - 1) {
      buf[bufpos] = 32;
      bufpos++;
    }
    if (bufpos < buflen - 1) {
      buf[bufpos] = 50;
      bufpos++;
    }
    if (bufpos < buflen - 1) {
      buf[bufpos] = 94;
      bufpos++;
    }
    exp -= 15;
    if (exp < 0 && bufpos < buflen - 1) {
      buf[bufpos] = 45;
      bufpos++;
    }
    exp = abs(exp);
    int dig = (exp >= 10 ? 2 : 1);
    while (dig > 0 && bufpos < buflen - 1) {
      buf[bufpos] = (exp / (dig == 3 ? 100 : (dig == 2 ? 10 : 1))) % 10 + 48;
      dig--;
      bufpos++;
    }
  }
  return buf;
}
/* This function converts an IEEE 32b floating point value into a 16b
   IEEE floating point value.  As a reminder: The sign bit is 1 bit,
   the exponent is 5 bits (with a bias of 15), and the significand is
   10 bits.

   There are several corner cases you need to make sure to consider:
   a) subnormal
   b) rounding:  We use round-to-even in case of a tie.
   c) rounding increasing the exponent on the significand.
   d) +/- 0, NaNs, +/- infinity.
 */
uint16_t as_ieee_16(union floating f)
{
  (void) f;
  int exp = ((f.as_int >> 23) & 0xFF);
  int sign = ((f.as_int >> 31) & 0x1);
  int fraction = (f.as_int) & 0x7FFFFF;
  if (exp == 255) {
    if (fraction == 0) {
      return (sign << 15) + (31 << 10);
    }
    else {
      return (sign << 15) + (31 << 10) + 1;
    }
  }
  else if (exp == 0) {
    return (sign << 15);
  }
  else {
    exp -= (127 - 15);
    if (exp < -11) {
      return (sign << 15);
    }
    int trunc = fraction & 0x1FFF;
    int mantissa = fraction >> 13;
    if (exp < 1) {
      if (trunc > (1 << 12)) {
        mantissa++;
      }
      else if (trunc == (1 << 12)) {
        mantissa += (mantissa & 1);
      }
      if (mantissa > (1 << 10)) {
        return (sign << 15) + (1 << 10);
      }
      else {
        return (sign << 15) + mantissa;
      }
    }
    else {
      if (trunc > (1 << 12) || (trunc == (1 << 12) && (mantissa & 1) == 0)) {
        exp += 1;
        mantissa >>= 1;
      }
      if (exp >= 31) {
        return (sign << 15) + (31 << 10);
      }
      else {
        return (sign << 15) + (exp << 10) + mantissa;
      }
    }
  }
  return 0;
}
