import random

def main(questtype,answer):
    af = ["./latin_stuff/dekli.txt","./latin_stuff/konju.txt","./latin_stuff/vokab.txt","./latin_stuff/gramm.txt"]
    list = []
    src = af[questtype]
    l = open(src, "r")
    for x in l:
        list.append(x)
    opt1,opt2,opt3,opt4,ans = sub(answer,list)
    return opt1,opt2,opt3,opt4,ans

def sub(answer,list):
    options = ["","","",""]
    options[0] = answer
    options[1] = subsub(list,answer)
    options[2] = subsub(list,answer)
    options[3] = subsub(list,answer)

    o = random.randint(0,3)
    opt1 = options[o]
    if opt1 == answer:
        ans = 1
    options.pop(o)
    o = random.randint(0,2)
    opt2 = options[o]
    if opt2 == answer:
        ans = 2
    options.pop(o)
    o = random.randint(0,1)
    opt3 = options[o]
    if opt3 == answer:
        ans = 3
    options.pop(o)
    o = 0
    opt4 = options[o]
    if opt4 == answer:
        ans = 4

    return opt1,opt2,opt3,opt4,ans

def subsub(list,answer):
    k = len(list)-1
    w = random.randint(0,k)
    splitted = list[w].split("-", 1)
    fina = splitted[1]
    fina = fina.replace('\n','')
    while fina == answer:
        w = random.randint(0,k)
        splitted = list[w].split("-", 1)
        fina = splitted[1]
        fina = fina.replace('\n','')
    list.pop(w)
    return fina
