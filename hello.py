def recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)
recursive_fib(40)
