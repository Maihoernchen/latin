import gui as gui
import chooser as choose
import time
import wrong_chooser as wrong

knew = True

question, caption, answer, questtype = choose.main()
opt1,opt2,opt3,opt4,ans = wrong.main(questtype, answer)
print(caption)
print(question)
print(opt1)
print(opt2)
print(opt3)
print(opt4)
print(ans)

while True:
    if ans != gui.main(caption, question, opt1, opt2, opt3, opt4):
        pass
    else:
        question, caption, answer, questtype = choose.main()
        opt1,opt2,opt3,opt4,ans = wrong.main(questtype, answer)
        print(caption)
        print(question)
        print(opt1)
        print(opt2)
        print(opt3)
        print(opt4)
        print(ans)
    time.sleep(300)
