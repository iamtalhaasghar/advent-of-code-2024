# red nosed reports

def is_safe(d, descending):
    if abs(d) < 1 or abs(d) > 3 or d==0:
        return False        
    if (descending and d < 0) or (not descending and d > 0):
        return False
    return True

s = 0
for r in open('data.txt').readlines():
    t = r.split()
    descending = True
    safe = True
    for i in range(len(t)-1):
        d = int(t[i]) - int(t[i+1])
        if i == 0 and d < 0:
            descending = False        
        if not is_safe(d, descending):
            safe = False
            break
    if safe:
        s+=1

print(s)

    
