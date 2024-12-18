
import re
t = open('data.txt').read()
def do_mul(t):
    s = 0
    d = re.findall(r'mul\((\d+),(\d+)\)', t)
    for a,b in d:
        s+= int(a) * int(b)
    return s
s = 0
r = 0
while True:
    e = t.find("don't()",s)
    r += do_mul(t[s:e]) # do multiplication until first don't
    if e == -1:
        break
    s = t.index("do()",e)
print(r)

