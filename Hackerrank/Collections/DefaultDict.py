'''
In this challenge, you will be given  integers,  and . There are  words, which might repeat, in word group . There are  words belonging to word group . For each  words, check whether the word has appeared in group  or not. Print the indices of each occurrence of  in group . If it does not appear, print .

Constraints 
 
 

Input Format

The first line contains integers,  and  separated by a space. 
The next  lines contains the words belonging to group . 
The next  lines contains the words belonging to group .

Output Format

Output  lines. 
The  line should contain the -indexed positions of the occurrences of the  word separated by spaces.

Sample Input

5 2
a
a
b
a
b
a
b
Sample Output

1 2 4
3 5
Explanation

'a' appeared  times in positions ,  and . 
'b' appeared  times in positions  and . 
In the sample problem, if 'c' also appeared in word group , you would print .
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
(n,m)=map(int, raw_input().split())
d=defaultdict(list)
for i in range(1,n+1):
    p=raw_input()
    d[p].append(i)
a=[]
for i in range(m):
    s = raw_input()
    if s in d:
        a=d[s]
        for f in a:
            print f,
        print ""
    else:
        print "-1"