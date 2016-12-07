'''
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.

Find the total number of distinct country stamps.

Input Format

The first line contains an integer , the total number of country stamps.
The next  lines contains the name of the country where the stamp is from. 
Constraints


Output Format

Output the total number of distinct country stamps on a single line.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
p = set()
count = 0
for i in range(n):
    M = raw_input()
    if M in p:
        continue
    else:
        p.add(M)
        count += 1
print count
        