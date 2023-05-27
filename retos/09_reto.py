is_prime = lambda n: all(n % i != 0 for i in range(2, n))

primes_up_to = lambda n: [i for i in range(2, n+1) if is_prime(i) == True]

print(primes_up_to(13))

