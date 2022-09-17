from pygame import mixer
from pytesseract import *
import pyautogui
import time

mixer.init()
mixer.music.load("RickRoll.wav")

# this is an empty list that will hold my subscounts 
subscribers = []

# for every sub I gain, this counter will increment
# the volume of the RickRoll audio file
counter = 0

while True: 
    # the location of pytesseract
    # replace my pytesseract path with your path on your computer
    pytesseract.tesseract_cmd = r'C:\Users\artde\AppData\Local\Tesseract-OCR\tesseract.exe'

    # takes a screenshot in the region where the subcount is located 
    SubCountScreenshot = pyautogui.screenshot(region=(1315,400, 250, 100))

    # the location of the scrreenshot
    # replace the image path with your path on your computer
    SubCountScreenshot.save(r"C:\Users\artde\Documents\Python Projects\SubCounter2.0\Subscribers.png")

    # saves the sub count as a string
    output = pytesseract.image_to_string(SubCountScreenshot)

    # removing the annoying ass coma from the subcount
    output = output.replace(',',"")

    # converting the subcount from a string to an integer
    currentSubcount = int(output)

    # with every loop, add a subscriber count to the list
    subscribers.append(currentSubcount)

    # if I gain subscribers print a message, play and increase
    # the volume of the audio and modify the list
    if subscribers[-1] > subscribers[0]:
        print("You gained subscribers!")
        counter += 0.3
        mixer.music.set_volume(0.1 * counter)
        mixer.music.play()
        subscribers[0] = subscribers[0] + 1

    # if I lose subscribers, print a message and modify the list
    elif subscribers[-1] < subscribers[0]:
        print("You lost subscribers!")
        subscribers[0] = subscribers[0] -1   

    # prints
    print(subscribers)

    time.sleep(10)


