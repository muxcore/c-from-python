import ctypes
import time

PRIME_ORDINAL = 1000_000 #  prime to get

# Path to DLL - change this!
dllPath = 'c:/home/code/clang/c-from-python/build/primeGenDLL.dll'

# Load the DLL
my_dll = ctypes.WinDLL(dllPath)

# Access the function from the DLL
my_function = my_dll.getPrime

# Specify the argument type(s)
my_function.argtypes = [ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]

# Define a variable to pass / store the result
pOrdinal = ctypes.c_size_t(PRIME_ORDINAL)
cumSum = ctypes.c_size_t()

# Access the updated value and  Rudimentary timing 
start_time=time.time()

# Call the function by passing the address of the variable
nthPrime = my_function(pOrdinal, ctypes.byref(cumSum))
print(PRIME_ORDINAL, "-Nth prime: ", nthPrime, sep="")
print("Sum of primes:", cumSum.value)

end_time=time.time()-start_time

print("Elapsed time (seconds):", end_time);
