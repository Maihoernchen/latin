import gui as gui
import chooser as choose
import time



while True:
    question, caption = choose.main(knew)
    gui.main(caption, question, answer)
    time.sleep(120)