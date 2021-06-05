

def fib(n):  # vrong prog, NOT DINAMIC
    if n <= 1:
        return n
    return (fib(n-1)+fib(n-2))



def fib(n): #DINAMIC prog
    fib = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        fib[i] =fib[i-1] + fib[i-2]
    return fib[n]

print(fib(50))