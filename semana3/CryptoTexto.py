test = int(input())
for c in range (0,test):
    certa = []
    msg = str(input())
    for l in msg :
        if l in ('abcdefghijklmnopqrstuvwxyz'):
            certa.append(l)
    rev = certa.reverse()
    sep = ''
    nv = sep.join(certa)
    print(nv)