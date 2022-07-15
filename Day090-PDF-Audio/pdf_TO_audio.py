from PyPDF2 import PdfFileReader
import pyttsx3

pdf='lion_rabbit.pdf'
file=open(pdf,'rb')
pdf_read=PdfFileReader(file)
pages=pdf_read.numPages
for i in range(0,pages):
    first_page=pdf_read.getPage(i)
    text=first_page.extractText()

    speak=pyttsx3.init()
    speak.say(text)
    speak.runAndWait()