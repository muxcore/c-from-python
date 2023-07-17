// Main DLL that will be called from Pyton.
// Not particulary efficient prime generator algorithm. We ignore offerflow possibility.

#define TRUE 1

inline int isPrime(size_t candidate)
{ 
  for (size_t i= 2; i * i <= candidate ; i++) {
    if (candidate % i == 0) {	  
      return 0;
    }
  }
  return 1; // candidate is prime number
} 

__declspec(dllexport)
size_t
getPrime(size_t nth, size_t *sum)
{
  size_t cntPrimesSeen = 0;
  size_t prime = 0;

  if (nth == 1) {
    *sum = 2;
    return 2;
  }
  if (nth == 2) {
    *sum = 5;
    return 3;
  }

  cntPrimesSeen = 2;
  *sum = 5;
  for (size_t i = 5; TRUE; i = i+2) {  
    if (isPrime(i)) {
      cntPrimesSeen++;
      *sum += i;
      if (cntPrimesSeen == nth) {
	prime = i;
	break;
      }
    }        
  } 
  return prime;
}
