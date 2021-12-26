import random

dekli = []
konju = []
vokab = []
gramm = []

d = open("./latin_stuff/dekli.txt", "r")
for x in d:
    dekli.append(x)

k = open("./latin_stuff/konju.txt", "r")
for x in k:
    konju.append(x)

v = open("./latin_stuff/vokab.txt", "r")
for x in v:
    vokab.append(x)

g = open("./latin_stuff/gramm.txt", "r")
for x in g:
    gramm.append(x)

print(dekli,konju,gramm,vokab)
def main(knew):
    if knew:
        questtype = random.randint(0,3)
        if questtype == 0:
            a = len(dekli)-1
            b = random.randint(0,a)
            splitted = dekli[b]
            question = dekli[b]
            caption = "Welche Deklination ist das?"
            dekli.pop(b)
            question.replace('\n','')
        elif questtype == 1:
            a = len(konju)-1
            b = random.randint(0,a)
            question = konju[b]
            caption = "Welche Konjugation ist das?"
            dekli.pop(b)
            question.replace('\n','')
        elif questtype == 2:
            a = len(vokab)-1
            b = random.randint(0,a)
            question = vokab[b]
            caption = "Was ist die deutsche Überseztung von...?"
            dekli.pop(b)
            question.replace('\n','')
        else:
            a = len(gramm)-1
            b = random.randint(0,a)
            question = gramm[b]
            caption = "Worum handelt es sich hier?"
            dekli.pop(b)
            question.replace('\n','')
    else:
        print("")
    return question, caption, answer

print(main(True))
