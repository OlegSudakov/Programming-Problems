# https://www.hackerrank.com/challenges/simple-text-editor

operations = []
s = ""

def append(w, record = True):
    global s
    s += w
    if record:
        operations.append(("a", len(w)))

def delete(k, record = True):
    global s
    if record:
        operations.append(("d", s[-k:]))
    s = s[:-k]
    
def undo():
    operation = operations.pop()
    type, val = operation
    if type == "a":
        delete(val, False)
    if type == "d":
        append(val, False)
        
q = int(input())
for i in range(q):
    line = input().strip().split(" ")
    try:
        t, val = line
        if t == "1":
            append(val)
        if t == "2":
            delete(int(val))
        if t == "3":
            print(s[int(val) - 1])
    except:
        t = line[0]
        if t == "4":
            undo()
