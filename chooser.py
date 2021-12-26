import random

dekli = []
konju = []
vokab = []
gramm = []

d = open("./dekli.txt", "r")
for x in d:
    dekli.append(x)

k = open("./konju.txt", "r")
for x in k:
    konju.append(x)

v = open("./vokab.txt", "r")
for x in v:
    vokab.append(x)

g = open("./gramm.txt", "r")
for x in g:
    gramm.append(x)

print(dekli,konju,gramm,vokab)
def main(knew):
    if knew:
        questtype = random.randint(0,3)
        if questtype == 0:
            a = len(dekli)-1
            b = random.randint(0,a)
            question = dekli[b]
            caption = "Welche Deklination ist das?"
            dekli.pop(b)
        elif questtype == 1:
            a = len(konju)-1
            question = konju[random.randint(0,len(konju)-1)]
            caption = "Welche Konjugation ist das?"
        elif questtype == 2:
            a = len(vokab)-1
            question = vokab[random.randint(0,len(vokab)-1)]
            caption = "Was ist die deutsche Überseztung von...?"
        else:
            a = len(gramm)-1
            question = gramm[random.randint(0,len(gramm)-1)]
            caption = "Worum handelt es sich hier"
    else:
        question = question
    return question, caption, answer

print(main(True))
