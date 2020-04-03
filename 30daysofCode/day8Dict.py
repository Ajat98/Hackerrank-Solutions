# Enter your code here. Read input from STDIN. Print output to STDOUT

d = {}
n = int(input())

for i in range(n):
    s = str(input()) 

    a = s.split()
    
    
    if a[0] not in d:
        d[a[0]] = int(a[1])


try:
    while True: 
        k = input()
        if k in d:
            print(str(k) + "=" + str(d[k]))
        else:
            print("Not found")
except EOFError:
    pass
