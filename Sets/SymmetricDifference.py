'''
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains an integer, . 
The second line contains  space-separated integers. 
The third line contains an integer, . 
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = raw_input()
s1= set(list(map(int,raw_input().split())))
n = raw_input()
s2= set(list(map(int,raw_input().split())))
p = s1.difference(s2).union(s2.difference(s1))
q = list(sorted(p))
for i in range(len(q)):
    print q[i]