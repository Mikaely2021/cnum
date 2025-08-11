import numpy as np

def is_perfect(n: int) -> bool:
    if n < 1:
        return False
    sum_divisors = 0

    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i

    return sum_divisors == n

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("O fatorial não está definido para números negativos")
        
    result = 1
    i = n
    while i > 1:
        result *= i
        i -= 1
    return result

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n: int) -> int:
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def 

def main():
    assert is_perfect(6) == True
    assert is_perfect(7) == False
    assert is_perfect(-1) == False
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert is_prime(7) == True
    assert is_prime(10) == False
    assert sum_of_digits(123) == 6
    print(C)
    print(C.shape)
    print(C.size) 
    print(len(C)) 
    try:
        factorial(-1)
    except ValueError as error:
        print(error) == "O fatorial não está definido para números negativos"
    try:
        sum_of_digits(-1)
    except ValueError as error:
        assert str(error) == "O número deve ser não negativo."
        
if __name__ == "__main__":
    main()
