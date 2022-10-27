# function for sieve of eratosthenes
def my_sieve(maximum):
    primes = []
    numbers = list(range(2, maximum))
    candidate = 2
    while candidate * candidate < maximum:
        for k in range(candidate, maximum, candidate):
            if k in numbers:
                numbers.remove(k)
        primes.append(candidate)
        # reset for new candidate
        candidate = numbers[0]
    return primes + numbers


print(my_sieve(50))
