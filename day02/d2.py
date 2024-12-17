# red nosed reports

def verify_diff(t):
    for i in range(len(t)-1):
        d = t[i] - t[i+1]
        if abs(d) < 1 or abs(d) > 3 or d==0:
            return False
    return True

s = 0
for r in open('data.txt').readlines():
    t = [int(i) for i in r.split()]
    if t == sorted(t) or t == sorted(t, reverse=True):
        # all ascending or descending
        if verify_diff(t):
            s+=1
            continue
    for i in range(len(t)):
        u = t.copy()
        u.pop(i)
        if u == sorted(u) or u == sorted(u, reverse=True):
            # all ascending or descending
            if verify_diff(u):
                s+=1
                break
print(s)

    
