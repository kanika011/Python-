'''
Task

You are given a string . 
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

Input Format

A single line containing the string  and integer value  separated by a space.

Constraints

 
The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string  on separate lines.

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = raw_input().split()
from itertools import combinations
for i in range(1,int(n[1])+1):
    for e in combinations(sorted(n[0]),i):print(''.join(e))
