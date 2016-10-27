'''Without using any string methods, try to print the following:


Note that "" represents the values in between.

Input Format 
The first line contains an integer .

Output Format 
Output the answer as explained in the task.
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(raw_input())
print ''.join(str(x) for x in xrange(1,a+1))