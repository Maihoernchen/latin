import gui as gui
import chooser as choose
import time
import wrong_chooser as wrong

i = 0
question, caption, answer, questtype = choose.main()
opt1,opt2,opt3,opt4,ans = wrong.main(questtype, answer)

while True:
    while i != 5:
        if ans != gui.main(caption, question, opt1, opt2, opt3, opt4):
            pass
        else:
            question, caption, answer, questtype = choose.main()
            opt1,opt2,opt3,opt4,ans = wrong.main(questtype, answer)
            i = i+1
    time.sleep(600)
    i = 0