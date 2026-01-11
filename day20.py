#Print prime numbers in range
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')

r=int(input("Enter the upper limit to print prime numbers up to: "))
print_primes_in_range(1, r)