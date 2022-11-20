from time import time
def is_prime(number:int):
    for x in range(2,number):
        if (number % x) == 0:
            return False
    return True

if __name__ == "__main__":
    start_time = time()
    count = 0
    for x in range(1,100001):
        if is_prime(x):
            count += 1
    print("1000000以内质数的个数是 ",count)
    end_time = time()
    print("整个程序用时:",end_time-start_time,"s")