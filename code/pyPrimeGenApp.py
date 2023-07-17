# Implementation of C algorithm in Python for comparisons

# Sieve of Atkin as an example of decent algorith
# def prime_generator(n):
#   """
#   Sieve of Atkin
#   Generates a list of primes up to n.
#   """
#   primes = []
#   sieve = [True] * (n + 1)
#   for i in range(2, int(math.sqrt(n)) + 1):
#     if sieve[i]:
#       primes.append(i)
#       for j in range(i * i, n + 1, i):
#         sieve[j] = False
#   return [2] + [p for p in range(3, n + 1) if sieve[p]]
import time
import math

PRIME_ORDINAL = 1000_00 #  prime to get

def isPrime(candidate):
  """Returns True if candidate is a prime number, False otherwise."""
  for i in range(2, int(math.sqrt(candidate)) + 1):
    if candidate % i == 0:
      return False
  return True


def getPrime(nth):
  """Returns the n-th prime number and its sum."""
  cntPrimesSeen = 0;
  prime = 0;
  suma = 0;

  # Maybe uncessary optimization?
  if nth == 1:
      suma = 2
      prime = 2
      return prime, suma

  if nth == 2:
      suma = 5
      prime = 3
      return prime, suma
    
  cntPrimesSeen = 2
  suma = 5
  i = 4
  while True:
      i += 1 
      if isPrime(i):
          cntPrimesSeen += 1
          suma += i
          if cntPrimesSeen == nth:
              prime = i
              break
  return prime, suma
     


# Rudimentary timing 
start_time=time.time()
print("Prime, Sum of primes:", getPrime(PRIME_ORDINAL))
end_time=time.time()-start_time
print("Elapsed time (seconds):", end_time);


# My results
# >>> 
# Prime, Sum of primes: (1299709, 62260698721)
# Elapsed time (seconds): 3.3059680461883545
# >>> 




