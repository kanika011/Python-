'''
You are given  numbers. Store them in a list and find the second largest number.

Input Format 
The first line contains . The second line contains an array [] of  integers each separated by a space.

Constraints 
 

Output Format 
Output the value of the second largest number.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

N=int(raw_input())
l=[]
p=raw_input().split()
a=b=c=None
for i in range(N):
    l.append(int(p[i]))
for n in l:
    if n>a:
        a,b,c = n,a,b
    elif a>n>b:
        b,c=n,b
    elif b>n>c:
        c=n
#print a,b,c
print b