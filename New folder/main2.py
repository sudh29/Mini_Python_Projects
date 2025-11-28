import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
for num in range(pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    voices = player.getProperty("voices")
    player.setProperty("voice", voices[1].id)

    # player.say(text)
    player.save_to_file(text, "audio.mp3")
    player.runAndWait()
