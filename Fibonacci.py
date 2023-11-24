def matrix_multiply(A, B):
    """Multiply two 2x2 matrices."""
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
    ]

def matrix_power(M, n):
    """Calculate the matrix M raised to the power n using recursion."""
    if n == 1:
        return M
    if n % 2 == 0:
        half_pow = matrix_power(M, n // 2)
        return matrix_multiply(half_pow, half_pow)
    else:
        return matrix_multiply(M, matrix_power(M, n - 1))

def fibonacci_matrix_exponentiation(n):
    """Calculate the nth Fibonacci number using matrix exponentiation."""
    if n == 0:
        return 0
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(base_matrix, n)
    return result_matrix[0][0]

fibsum = 0
n = 1
result = 0
uppervalue = 4000000

while result <= uppervalue:
    result = fibonacci_matrix_exponentiation(n)
    if (result % 2) == 0 and result <= uppervalue:
        fibsum = fibsum + result
    n = n + 1

print(f"The sum of even valued Fibonacci numbers, considering the terms in the Fibonacci sequence whose values do not exceed {uppervalue} is: {fibsum}")