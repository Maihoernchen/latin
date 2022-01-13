import random

def main(questtype,answer):
    af = ["./latin_stuff/dekli.txt","./latin_stuff/konju.txt","./latin_stuff/vokab.txt","./latin_stuff/gramm.txt"]
    list = []
    src = af[questtype]
    l = open(src, "r")
    for x in l:
        list.append(x)
    options,ans = sub(answer,list)
    opt1 = options[0]
    opt2 = options[1]
    opt3 = options[2]
    opt4 = options[3]
    return opt1,opt2,opt3,opt4,ans

def sub(answer,list):
    options = ["","","",""]
    options[0] = answer
    options[1] = subsub(list,answer)
    options[2] = subsub(list,answer)
    options[3] = subsub(list,answer)
    random.shuffle(options)

    if options[0] == answer:
        ans = 1
    if options[1] == answer:
        ans = 2
    if options[2] == answer:
        ans = 3
    if options[3] == answer:
        ans = 4

    return options,ans

def subsub(list,answer):
    k = len(list)-1
    w = random.randint(0,k)
    splitted = list[w].split("-", 1)
    fina = splitted[1]
    fina = fina.replace('\n','')
    while fina == answer or fina in options:
        w = random.randint(0,k)
        splitted = list[w].split("-", 1)
        fina = splitted[1]
        fina = fina.replace('\n','')
    list.pop(w)
    return fina
