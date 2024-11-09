from functools import lru_cache
import time

@lru_cache
def fib(n:int) -> int:
    if(n<=1):
        return n
    else:
        return fib(n-1)+fib(n-2)

n=int(input("Enter Range : "))

start_time = time.time()

for i in range(0,n):
    print(f'{i}: {fib(i)}')

end_time = time.time()

elapsed_time = end_time - start_time
print(f"\nTime taken: {elapsed_time:.4f} seconds")