aimport gui as gui
import chooser as choose
import time

knew = True

while True:
    question, caption, answer = choose.main()
    gui.main(caption, question, answer)
    time.sleep(120)
