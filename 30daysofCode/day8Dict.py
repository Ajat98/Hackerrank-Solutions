# Enter your code here. Read input from STDIN. Print output to STDOUT


d = {}
n = int(input())

for i in range(n):
    s = input() 

    a = s.split(" ")
    
    
    if a[0] not in d:
        d[a[0]] = int(a[1])


for i in range(n): 
    k = input()
    if k in d.keys():
        print(str(k) + "=" + str(d[k]))
    else:
        print("Not found")

