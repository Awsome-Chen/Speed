import taichi as ti
ti.init(arch=ti.cpu)
from time import time
@ti.func
def is_prime(n: int):
    result = True
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            result = False
            break
    return result

@ti.kernel
def count_primes(n: int) -> int:
    count = 0
    for k in range(2, n):
        if is_prime(k):
            count += 1

    return count

if __name__=="__main__":
    start_time = time()
    print(count_primes(100000))
    end_time = time()
    print("整个程序用时:",end_time-start_time,"s")