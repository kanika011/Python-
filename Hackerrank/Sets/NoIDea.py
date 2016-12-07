'''
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints 
 
 

Input Format

The first line contains integers  and  separated by a space. 
The second line contains  integers, the elements of the array. 
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
'''
n = raw_input()
S = (map(int, raw_input().split()))
A = set(list(map(int, raw_input().split())))
B = set(list(map(int, raw_input().split())))
result = 0
for l in S:
    if l in A:
        result += 1
    if l in B:
        result -= 1
print  result