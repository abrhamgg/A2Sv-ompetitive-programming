size = input()
size = size.split(' ')
m = size[0]
n = size[1]
if m is not int:
    m = int(size[0])
if n is not int:
    n = int(size[1])    

if (m and n):
    print((m * n) // 2)
