#   ____      ____   ___   ____  _____  ________
#  |_  _|    |_  _|.'   `.|_   \|_   _||_   __  |
#    \ \  /\  / / /  .-.  \ |   \ | |    | |_ \_|
#     \ \/  \/ /  | |   | | | |\ \| |    |  _| _
#      \  /\  /   \  `-'  /_| |_\   |_  _| |__/ |
#       \/  \/     `.___.'|_____|\____||________|
#
# source:http://patorjk.com/software/taag/#p=author&f=Varsity&t=wone

"""This module is being made to act as a store for all python functions"""
# todo to convert the code into Classes

"""
Index:
gtts #Google Text To Speech
mypy #for annotation checking (there is a typing library also available)
timeit #need to study this
"""


def text2speech(textString: str) -> None:
    """Google Text To Speech Library.  Used the mypy Library"""

    from gtts import gTTS  # Import the required module for text to speech conversion
    import os  # This module is imported so that we can play the converted audio
    import sys

    mytext = textString  # The text that you want to convert to audio
    language = "en"  # Language in which you want to convert

    myobj = gTTS(
        text=mytext, lang=language, slow=False
    )  # Passing the text and language to the engine,here we have marked slow=False. Which tells the module that the converted audio should have a high speed
    myobj.save(
        "theConvertedSpeech.mp3"
    )  # Saving the converted audio in a mp3 file named welcome
    os.system("theConvertedSpeech.mp3")  # Playing the converted file

    # sys.exit()

def checkErrorUsingPDB():
    import pdb

    pdb.set_trace()  # simple options are next, continue, run


def p(*args):
    print(f"Value of {args} is ", end="")
    print(args)  # These print are used to be later on deleted)


def bell():
    import winsound

    duration = 3000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)




# import datetime
#
#
# a = datetime.datetime
# print(type(a))
# print(dir(type(a)))
#
# for x in list(dir(type(a))):
#     print(x)
#