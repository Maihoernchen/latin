import gui as gui
import chooser as choose
import time

i = 0
question, caption, answer, answers = choose.main()
while True:
    while i != 5:
        if answer != answers[gui.main(caption, question, answers)]:
            pass
        else:
            question, caption, answer, answers = choose.main()
            i = i+1
    gui.quit()
    time.sleep(300)
    i = 0