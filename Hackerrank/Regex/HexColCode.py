'''
CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code

■ It must start with a '#' symbol.
■ It can have  or  digits.
■ Each digit is in the range of  to . ( and ).
■  letters can be lower case. ( and  are also valid digits).

Examples

Valid Hex Color Codes
#FFF 
#025 
#F0A1FB 

Invalid Hex Color Codes
#fffabg
#abcf
#12365erff
You are given  lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

CSS Code Pattern

Selector
{
	Property: Value;
}
Input Format

The first line contains , the number of code lines.
The next  lines contains CSS Codes.

Constraints



Output Format

Output the color codes with '#' symbols on separate lines.

Sample Input

11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   
Sample Output

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys
if sys.version_info[0]>=3: raw_input = input
inside_css =False
n = raw_input()
s=""
for i in range(int(n)):
    s = raw_input().strip()
    if not s:
        pass
    elif s[-1] == '{':
        inside_css =True
    elif s[-1] == '}':
        inside_css = False
    elif inside_css:
        for e in re.finditer(r'#[0-9A-Fa-f]{3,6}',s):
            if len(e.group(0))==4 or len(e.group(0)) ==7: print(e.group(0))