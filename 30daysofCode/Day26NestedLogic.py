# Enter your code here. Read input from STDIN. Print output to STDOUT



rd, rm, ry = [int(t) for t in input().split(' ')]
ed, em, ey = [int(t) for t in input().split(' ')]

fine = 0
if ry > ey:
    print(10000)
elif ry == ey and rm>em:
    print( (rm-em)*500 )
elif ry == ey and rm == em and rd > ed:
    print((rd - ed)*15)
else:
    print(0)


