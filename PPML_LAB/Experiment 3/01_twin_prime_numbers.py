# Program 1: Print twin prime numbers between 1 and N
N = int(input("Enter the upper limit N: "))
def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False
    return True
print("Twin prime pairs:")
for number in range(2, N - 1):
    if is_prime(number) and is_prime(number + 2) and number + 2 <= N:
        print((number, number + 2))
