with open('input.txt') as f:
    data = f.read().split('\n')

executed = []
bad_rules = {n for n, i in enumerate(data) if i.startswith(('jmp', 'nop'))}
accu = 0
         
def execute(ln):
    if ln in executed:
        return None
    cmd, val = data[ln].split()
    val = int(val)
    executed.append(ln)
    global accu
    print(ln, cmd, val, accu)
    if cmd == 'acc':
        accu += val
        if ln+1 < len(data):
            execute(ln+1)

    elif cmd == 'jmp':
        if ln+val < len(data):
            execute(ln+val)
    else:
        execute(ln+1)
    

execute(0)
