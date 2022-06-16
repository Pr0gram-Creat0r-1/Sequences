def fibonacci(n):
    'Return nth term of Fibonacci Sequence.'
    fib_list = [0, 1]
    loop_number = n - 2
    for x in range(0, loop_number):
        fib_list.append(fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2])
    return fib_list
def prime_numbers(n):
    'Return the nth prime number starting from 2.'
    prime_list = []
    number = 2
    while len(prime_list) < n:
        factor = 2
        composite_bool = 0
        while factor < number:
            if number % factor == 0:
                composite_bool = 1
                break
            factor += 1
        if composite_bool == 0:
            prime_list.append(number)
        number += 1
    return prime_list
def is_prime(number):
    'Check if a number is prime.'
    factor = 2
    composite_bool  = 0
    while factor < number:
        if number % factor == 0:
            composite_bool = 1
            return False
            break
        factor += 1
    if composite_bool == 0:
        return True
def mersenne(n):
    'Return the nth Mersenne prime and the power of 2 it is based off of.'
    mersenne_list = []
    power = 2
    number = 2
    while len(mersenne_list) < n:
        number = 2 ** power
        if is_prime(number - 1):
            mersenne_list.append(number - 1)
        power += 1
    return [mersenne_list, power - 1]
def is_mersenne(number):
    'Check if number is a Mersenne prime.'
    power = 2
    power_number = 2
    while power_number <= number:
        power_number = 2 ** power
        power += 1
    if is_prime(number) and power_number - 1 == number:
        return True
    else:
        return False
def sequence(terms, start, end):
    'Create a list of ordered pairs. Depending on the length of the list in the "terms" argument, the function will return for a constant, arithmetic, quadratic, etc. sequence.'
    x = start
    table = []
    while x <= end:
        counter = 0
        power = len(terms) - 1
        _sum = 0
        for y in range(0, len(terms)):
            _sum += terms[counter] * (x ** power)
            power -= 1
            counter += 1
        table.append(_sum)
        x += 1
    return table
def geo_sequence(term1, term2, start, end):
    'Create a geometric sequence (f(n) = a * b^n). term1 is a and term2 is b.'
    x = start
    table = []
    while x <= end:
        table.append(term1 * (term2 ** x))
        x += 1
    return table
