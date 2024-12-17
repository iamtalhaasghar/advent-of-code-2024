# advent of code day 01 - Historian hysteria
# iamtalhaasghar

lines = open('data.txt').readlines()
left = []
right = []
for l in lines:
    t = l.split()
    left.append(int(t[0]))
    right.append(int(t[1]))
left = sorted(left)
right = sorted(right)
d = 0
for i in range(len(left)):
    d+= abs(left[i] - right[i])
print(d)

s = 0
for i in left:
    s+= i * right.count(i)
print(s)
