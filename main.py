"""
Given n as input. Print following pattern using For loop.
n = 2
Expected Output:
#
#
2
1
"""

n = 5
pt = "#"
for i in range(1, n+1):
  print(pt)
for i in range(n, 0, -1):
  print(i)