'''Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid. You have to print a list of all possible coordinates on a 3D grid where the sum of      is not equal to . If , the possible values of  can be ,  and . The same applies to  and .

Input Format

Four integers  and  each on four separate lines, respectively.

Output Format

Print the list in lexicographic increasing order.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
X=int(raw_input())
Y=int(raw_input())
Z=int(raw_input())
N=int(raw_input())
l=[[x,y,z] for x in range(X + 1) for y in range(Y + 1) for z in range(Z + 1) if x+y+z != N]
print l