import random
import time

dekli = []
konju = []
vokab = []
gramm = []


def main(knew):
    if knew:
        questtype = random.randint(0,3)
        if questtype == 0:
            try:
                a = len(dekli)-1
                b = random.randint(0,a)
                splitted = dekli[b].split(" ", 1)
                question = splitted[0]
                answer = splitted[1]
                caption = "Welche Deklination ist das?"
                dekli.pop(b)
                answer = answer.replace('\n',''  )
            except:
                d = open("./latin_stuff/dekli.txt", "r")
                for x in d:
                    dekli.append(x)
        elif questtype == 1:
            try:
                a = len(konju)-1
                b = random.randint(0,a)
                splitted = konju[b].split(" ", 1)
                question = splitted[0]
                answer = splitted[1]
                caption = "Welche Konjugation ist das?"
                konju.pop(b)
                answer = answer.replace('\n',''  )
            except:
                k = open("./latin_stuff/konju.txt", "r")
                for x in k:
                    konju.append(x)
        elif questtype == 2:
            try:
                a = len(vokab)-1
                b = random.randint(0,a)
                splitted = vokab[b].split(" ", 1)
                question = splitted[0]
                answer = splitted[1]
                caption = "Was ist die deutsche Überseztung von...?"
                vokab.pop(b)
                answer = answer.replace('\n',''  )
            except:
                v = open("./latin_stuff/vokab.txt", "r")
                for x in v:
                    vokab.append(x)
        else:
            try:
                a = len(gramm)-1
                b = random.randint(0,a)
                splitted = gramm[b].split(" ", 1)
                question = splitted[0]
                answer = splitted[1]
                caption = "Worum handelt es sich hier?"
                gramm.pop(b)
                answer = answer.replace('\n',''  )
            except:
                g = open("./latin_stuff/gramm.txt", "r")
                for x in g:
                    gramm.append(x)
    else:
        pass
    try:
        return question, caption, answer
    except:
        pass
