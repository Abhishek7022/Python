def checkns(mys):
    u, l, i = 0, 0, 0
    while i < len(mys):
        if mys[i].isupper():
            u += 1
        elif mys[i].islower():
            l += 1
        else:
            pass
        i += 1
    print('No. of uppercase characters: {}'.format(u))
    print('No. of lowercase characters: {}'.format(l))

checkns('Hello Mr. Rogers, how are you this fine Tuesday?')


def nlist(mylist):
    return list(set(mylist))

mlist = [1,1,1,1,1,2,2,2,4,4,6,7,6,7,8,6,9,6,9,0,6,12,11,11,2,12]
print(nlist(mlist))

def muln(lst):
    i, u = 0, 1
    while i < len(lst):
        u = lst[i]*u
        i += 1
    return u

nlist = [1,2,3,-4]
print(muln(nlist))


def panda(sstr):
    i = 0
    while i < len(sstr):
        if sstr[i] in 'abcdefghijklmnopqrstuvwxyz':
            return True
        i += 1
    return False

neww = 'The quick brown fox jumps over the lazy dog'
print(list(set(filter(panda, neww))))