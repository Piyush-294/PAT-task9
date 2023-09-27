# Function to generate a Fibonacci series using lambda function
from functools import reduce

fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

# Input the number of terms you want in the Fibonacci series
n = int(input("Enter the number of terms in the Fibonacci series: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    # Generate the Fibonacci series
    fib_series = fibonacci(n)

    # Print the Fibonacci series
    print("Fibonacci Series:")
    print(fib_series)
