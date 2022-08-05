import json

print("Welche Kategorie?", "\n", "1: Deklinationen", "\n", "2: Grammatik","\n", "3: Konjugationen","\n", "4: Vokabeln", "\n")
kat = input("")
katList = ["./latin_stuff/dekli.json","./latin_stuff/gramm.json","./latin_stuff/konju.json","./latin_stuff/vokab.json"]
chosKat = katList[int(kat)-1]
while True:
    print("Lateinische Phrase?","\n")
    question = input("")
    print("Antwort?","\n")
    answer = input("")
    if "," in answer:
        answer = answer.split(",")
    with open(chosKat, "r+") as l:
        data = json.load(l)

        data[question] = answer

        print(data)
        l.seek(0)
        json.dump(data,l)
        l.truncate()