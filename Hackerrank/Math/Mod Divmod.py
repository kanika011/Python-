'''
Read in two integers,  and , and print three lines. 
The first line is the integer division  (While using Python2 remember to import division from __future__). 
The second line is the result of the modulo operator: . 
The third line prints the divmod of  and .

Input Format 
The first line contains the first integer, , and the second line contains the second integer, .

Output Format 
Print the result as described above.

'''



from __future__ import division
n = int(raw_input())
p = int(raw_input())
print int(n/p)
print n%p
print divmod(n,p)