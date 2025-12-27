import stdio
# read all strings from terminal and write them in reverse order

a = stdio.readAllStrings()
n = len(a)
for i in range(n//2):
    temp = a [i]
    a[i] = a[n - i - 1]
    a[n - i - 1] = temp 
for i in range(n):
    if i < n - 1: 
        stdio. write(a[i] + ' ')
    else:
        stdio.writeln(a[i] + ' ')




