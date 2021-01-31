# rd is returned day
# rm is returned month
# ry is returned year
# dd, dm and dy are due date, due month and due year respectively

rd, rm, ry = [int(x) for x in input().split(' ')]
dd, dm, dy = [int(x) for x in input().split(' ')]

if ry > dy:
    print(10000)
elif (rd < dd and rm == dm and ry == dy):
    print(0)
elif (rd < dd and rm < dm and ry == dy):
    print(0)
elif ((rd > dd and rm < dm and ry < dy) or (rd<dd and ry <dy) or (rd > dd and rm>dm and ry <dy)):
    print(0)
elif (rd > dd and rm == dm and ry == dy):
    val = rd - dd
    print (15 * val)
elif (rd > dd and rm > dm and ry == dy):
    val2 = rm - dm
    print (val2 * 500)