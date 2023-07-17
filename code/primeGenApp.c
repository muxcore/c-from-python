// Used in testing, can be ignored for calling from python.
// Compile if you want to run prime generator as standalone .exe


#include <stdio.h>
#include "primeGenDLL.c"

int main(int argc, char **argv) {

  // we allow only 1 command line argument
  if(argc != 2) {
    fprintf(stderr, "Usage: %s [nthPrime]\n", argv[0]);
    return 1;
  }
  
  int nth = (int)strtol(argv[1], NULL, 10);  
  size_t prime = 0;
  size_t sum = 0; // important to initialize
  
  prime = getPrime(nth, &sum);
  printf("%d-th prime is: %zd, and cumSum is: %zd\n", nth, prime, sum);
  
  return 0;
}

