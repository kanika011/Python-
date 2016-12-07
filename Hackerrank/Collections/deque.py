'''
erform append, pop, popleft and appendleft methods on an empty deque .

Input Format

The first line contains an integer , the number of operations. 
The next  lines contains the space separated names of methods and their values.

Constraints


Output Format

Print the space separated elements of deque .

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output

1 2

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(raw_input())
d = deque()
for i in range(n):
    p = raw_input().split()
    if p[0] == 'pop':
        d.pop()
    if p[0] == 'popleft':
        d.popleft()
    if p[0] == 'append':
        d.append(p[1])
    if p[0] == 'appendleft':
        d.appendleft(p[1])
for i in d:
    print i,