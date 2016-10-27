'''Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands. 
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.'''


l=[]
N = int(raw_input())
while N >0:
    N -=1
    p = raw_input().split()
    if p[0] == 'insert':
        l.insert(int(p[1]), int(p[2]))
        #print l
    if p[0] == 'print':
        print l
    if p[0] == 'pop':
        l.pop()
        #print l
    if p[0] == 'remove':
        l.remove(int(p[1]))
        #print l
    if p[0] == 'reverse':
        l.reverse()
        #print l
    if p[0] == 'sort':
        l.sort()
        #print l
    if p[0] == 'append':
        l.append(int(p[1]))
        #print l
    