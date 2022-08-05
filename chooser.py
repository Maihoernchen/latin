import random
import time
import json


def openfile(src):

    l = open(src, "r")
    l = json.load(l)
    return l

def pick_from_list(dict,cap):
    list = []
    for x in dict:
        list.append(x)
    a = len(list)-1
    b = random.randint(0,a)
    question = list[b]
    answer = dict[question]
    caption = cap
    list.pop(b)
    answers = [answer]
    i = 0
    while i < 3:
        a = len(list)-1
        b = random.randint(0,a)
        if dict[list[b]] not in answers:
            answers.append(dict[list[b]])
            list.pop(b)
            i+=1
    random.shuffle(answers)
    return question,caption,answer,answers

def main():
    dekli = []
    konju = []
    vokab = []
    gramm = []
    questtype = random.randint(0,3)
    if questtype == 0:
        if len(dekli) == 0:
            dekli = openfile("./latin_stuff/dekli.json")
        list = dekli
        cap = "Welche Deklination ist das?"
    elif questtype == 1:
        if len(konju) == 0:
            konju = openfile("./latin_stuff/konju.json")
        list = konju
        cap = "Welche Konjugation ist das?"
    elif questtype == 2:
        if len(vokab) == 0:
            vokab = openfile("./latin_stuff/vokab.json")
        list = vokab
        cap = "Wie heißt das auf Deutsch?"
    else:
        if len(gramm) == 0:
            gramm = openfile("./latin_stuff/gramm.json")
        list = gramm
        cap = "Worum handelt es sich hier?"
    question,caption,answer,answers = pick_from_list(list,cap)
    return question, caption, answer, answers
