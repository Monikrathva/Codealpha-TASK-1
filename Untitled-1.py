def fibonaaci(n):

    fib_series = []

    a = 0
    b = 1

    fib_series.append(a)
    fib_series.append(b)

    for i in range (2,n):

        next_number = a + b

        fib_series.append(next_number)

        a = b
        b = next_number
        
    return fib_series
print(fibonaaci(10))    