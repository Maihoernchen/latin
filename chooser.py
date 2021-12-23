import random

dekli = []
konju = []
vokab = []
gramm = []

d = open("dekli.txt", "r")
for x in d:
  dekli[x] = x

k = open("konju.txt", "r")
for x in k:
  konju[x] = x

v = open("vokab.txt", "r")
for x in v:
  dekli[x] = x

g = open("gramm.txt", "r")
for x in g:
  dekli[x] = x


def main(knew):
    if knew:
        questtype = random.randint(0,3)
        if questtype == 0:
            question = dekli[random.randint(0,len(dekli)-1)]
            caption = "Welche Deklination ist das?"
            answer
        elif questtype == 1:
            question = konju[random.randint(0,len(konju)-1)]
            caption = "Welche Konjugation ist das?"
        elif questtype == 2:
            question = vokab[random.randint(0,len(vokab)-1)]
            caption = "Was ist die deutsche Überseztung von...?"
        else:
            question = gramm[random.randint(0,len(gramm)-1)]
            caption = "Worum handelt es sich hier"
    else:
        question = question
    return question, caption