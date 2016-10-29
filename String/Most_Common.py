'''
You are given a string . 
The string contains only lowercase English alphabet characters.

Your task is to find the top three most common characters in the string .

Input Format

A single line of input containing the string .

Constraints


Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in ascending order.

Sample Input

aabbbccde
Sample Output

b 3
a 2
c 2
Explanation

Here, b occurs  times. It is printed first.
Both a and c occur  times. So, a is printed in the second line and c in the third line because a comes before c.

Note: The string  has at least  distinct characters.
'''

n = raw_input()
d = {}
for i in n:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
for i in sorted(d.items(), key=lambda x:(-x[1], x[0]))[:3]:
    print i[0], i[1]
