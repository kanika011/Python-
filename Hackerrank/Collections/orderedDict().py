'''
You are the manager of a supermarket. 
You have a list of  items together with their prices that consumers bought on a particular day. 
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item. 
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format

The first line contains the number of items, . 
The next  lines contains the item's name and price, separated by a space.

Constraints


Output Format

Print the item_name and net_price in order of its first occurrence.

Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(raw_input())
items = []
for i in range(n):
    entry = raw_input().strip().split()
    name = (" ").join(entry[0:(len(entry)-1)])
    price = int(entry[len(entry)-1])
    items.append((name, price))
d = OrderedDict()
for name, price in items:
    if name in d:
        d[name]+= price
    else:
        d[name] = price
for name, price in d.items():
    print name, price