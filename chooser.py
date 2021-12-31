import random
import time



def restore_arrays(src,list):

    l = open(src, "r")
    for x in l:
        list.append(x)
    return list

def pick_from_list(list,cap):

    a = len(list)-1
    b = random.randint(0,a)
    splitted = list[b].split("-", 1)
    question = splitted[0]
    answer = splitted[1]
    caption = cap
    list.pop(b)
    answer = answer.replace('\n',''  )
    return question,caption,answer

def main():
    dekli = []
    konju = []
    vokab = []
    gramm = []
    questtype = random.randint(0,3)
    if questtype == 0:
        if len(dekli) == 0:
            dekli = restore_arrays("./latin_stuff/dekli.txt",dekli)
        question,caption,answer = pick_from_list(dekli,"Welche Deklination ist das?")
    elif questtype == 1:
        if len(konju) == 0:
            konju = restore_arrays("./latin_stuff/konju.txt",konju)
        question,caption,answer = pick_from_list(konju,"Welche Konjugation ist das?")
    elif questtype == 2:
        if len(vokab) == 0:
            vokab = restore_arrays("./latin_stuff/vokab.txt",vokab)
        question,caption,answer = pick_from_list(vokab,"Wie heißt das auf Deutsch?")
    else:
        if len(gramm) == 0:
            gramm = restore_arrays("./latin_stuff/gramm.txt",gramm)
        question,caption,answer = pick_from_list(gramm,"Worum handelt es sich hier?")
    return question, caption, answer, questtype
