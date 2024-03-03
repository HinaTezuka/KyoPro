import math

def sieve_of_eratosthenes(n):
    cache = [True] * n

    for currentPrime in range(2, math.ceil(math.sqrt(n))):
        if not cache[currentPrime]: continue
        i = 2
        ip = i * currentPrime

        while ip < n:
            cache[ip] = False
            i += 1
            ip = i * currentPrime
    
    primes = []
    for index, predicate in enumerate(cache):
        if predicate: primes.append(index)
    
    return primes[2:]

print(sieve_of_eratosthenes(3))