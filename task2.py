# Foster Cavender
# CS1400 online 7 week

import drawly
from moody import Moody

def main():
    drawly.start("Dr. Moody")

    start_smile = True
    start_happy = True
    start_dark_eyes = True

    professor = Moody(start_smile, start_happy, start_dark_eyes)
    professor.draw_face()

    done = False

    print("Welcome to Dr. Moody!!!")
    print()

    while not done:
        print("Change My Face")
        mouth = "frown" if professor.is_smile() else "smile"
        emotion = "angry" if professor.is_happy() else "happy"
        eyes = "green" if professor.is_dark_eyes() else "black"
        print("\t1) Make me", mouth)
        print("\t2) Make me", emotion)
        print("\t3) Make my eyes", eyes)
        print("\t0) Quit")

        menu = int(input("Enter a selection: "))

        if menu == 1:
            professor.change_mouth()
        elif menu == 2:
            professor.change_emotion()
        elif menu == 3:
            professor.change_eyes()
        else:
            done = True

    print("Thanks for Playing")
    drawly.done()

main()
