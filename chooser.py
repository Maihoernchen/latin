import random

dekli = []
konju = []
vokab = []
gramm = []

d = open("C:\\Users\Atom\Documents\School fuckujd\latein\latin_stuff\dekli.txt", "r")
for x in d:
  dekli.append(x)

k = open("C:\\Users\Atom\Documents\School fuckujd\latein\latin_stuff\konju.txt", "r")
for x in k:
  konju.append(x)

v = open("C:\\Users\Atom\Documents\School fuckujd\latein\latin_stuff\\vokab.txt", "r")
for x in v:
  vokab.append(x)

g = open("C:\\Users\Atom\Documents\School fuckujd\latein\latin_stuff\gramm.txt", "r")
for x in g:
  gramm.append(x)

print(dekli,konju,gramm,vokab)
def main(knew):
    if knew:
        questtype = random.randint(0,3)
        if questtype == 0:
            a = len(dekli)-1
            question = dekli[random.randint(0,a)]
            caption = "Welche Deklination ist das?"
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