def sieve_prime_number(sieve_limit):
    is_prime = [True] * (sieve_limit + 1)

    number_to_test = 2
    while number_to_test * number_to_test <= sieve_limit:
        if is_prime[number_to_test]:
            multiple_to_mark_as_not_prime = 2 * number_to_test
            while multiple_to_mark_as_not_prime <= sieve_limit:
                is_prime[multiple_to_mark_as_not_prime] = False
                multiple_to_mark_as_not_prime += number_to_test
        number_to_test += 1

    # Extract from is_prime list the list of prime number

    prime_number_list = []
    number_to_test = 2
    while number_to_test <= sieve_limit:
        if is_prime[number_to_test]:
            prime_number_list.append(number_to_test)
        number_to_test += 1

    return prime_number_list


def sieve_prime_number_odd(sieve_limit):
    # Optimization based on the fact that only 2 is an even primary number
    is_prime = [True] * (sieve_limit//2-1)

    number_to_test = 3
    while number_to_test * number_to_test <= sieve_limit:
        if is_prime[number_to_test//2-1]:
            multiple_to_mark_as_not_prime = 3 * number_to_test
            while multiple_to_mark_as_not_prime <= sieve_limit:
                is_prime[multiple_to_mark_as_not_prime//2-1] = False
                multiple_to_mark_as_not_prime += number_to_test*2
        number_to_test += 2

    # Transformation the is_prime in a list of prime number

    prime_number_list = [2]
    number_to_test = 0
    while number_to_test <= (sieve_limit//2-2):
        if is_prime[number_to_test]:
            prime_number_list.append(number_to_test*2+3)
        number_to_test += 1

    return prime_number_list


print(sieve_prime_number_odd(100))