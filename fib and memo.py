# fibonacci sequence and memoization

# fibonacci fuction without memoization

def fibonacci(n):
    # Check if the n is positive integer

    if not isinstance(n, int):
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")

    # comput the nth term
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# for n in range(1, 101):  # very slow
#    print(n, " : ", fibonacci(n))

    

# use memo

memo = {}

def fib_memo(n):
    # Check if the n is positive integer

    if not isinstance(n, int):
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    # if we have cached value, then return it
    if n in memo:
        return memo[n]

    # comput the nth term
    if n == 1 or n == 2:
        value =  1
    else:
        value = fib_memo(n - 1) + fib_memo(n - 2)

    # cache the value and return it
    memo[n] = value
    return value


# for n in range(1, 1001):
#    print(n, " : ", fib_memo(n))



# using lru_cache


from functools import lru_cache


@lru_cache(maxsize = 1000)
def fib_lru(n):
    # Check if the n is positive integer

    if not isinstance(n, int):
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")
    

    # comput the nth term
    if n == 1 or n == 2:
        return 1
    else:
        return fib_lru(n - 1) + fib_lru(n - 2)



for n in range(1, 1001):
    print(n, " : ", fib_lru(n))

