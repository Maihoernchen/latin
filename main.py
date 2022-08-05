import gui as gui
import chooser as choose
import time
import wrong_chooser as wrong

i = 0
question, caption, answer, answers = choose.main()

while True:
    while i != 5:
        if answer != gui.main(caption, question, answers):
            pass
        else:
            question, caption, answer, answers = choose.main()
            i = i+1
    time.sleep(600)
    i = 0