# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

def prime(n):
    if n == 1 or n ==0:
        return 'Not prime'

    i = 2
    while i*i <= n:
        # Check if i divides x without remainder, increments i by 1 until it is at sqrt(n)
        if n%i ==0:
            return 'Not prime'
        i +=1
    return 'Prime'

for i in range(t):
    n = int(input())

    print(prime(n))

    
