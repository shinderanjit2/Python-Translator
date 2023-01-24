import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

print("1 Hindi")
print("2 Marathi")
print("3 Spanish")
print("4 German")
print("5 Russian")
print("6 French")
print("Choose language to convert : ")
ch = int(input())

if ch == 1:
    print("Your Speech Will Be Translated Into Hindi")
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say Something:')
        audio = r.listen(source)
        print('Done!')

        text = r.recognize_google(audio, language='en-IN')
        print("You Said : ", text)
        translater = Translator()
        out = translater.translate(text, dest="hi")
        print("Hindi Translation : ", out.text)

        language = 'hi'
        output = gTTS(text=out.text, lang=language, slow=False)
        output.save("output.mp3")
        # Play the converted file
        os.system("output.mp3")

elif ch == 2:
    print("Your Speech Will Be Translated Into Marathi")
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say Something:')
        audio = r.listen(source)
        print('Done!')

    text = r.recognize_google(audio, language='en-IN')
    print("You Said : ", text)

    translater = Translator()
    out = translater.translate(text, dest="mr")
    print("Marathi Translation : ", out.text)

    language = 'mr'
    output = gTTS(text=out.text, lang=language, slow=False)
    output.save("output.mp3")
    # Play the converted file
    os.system("start output.mp3")

elif ch == 3:
    r = sr.Recognizer()
    print("Your Speech Will Be Translated Into Spanish")
    with sr.Microphone() as source:

        print('Say Something:')
        audio = r.listen(source)
        print('Done!')

    text = r.recognize_google(audio, language='en-IN')
    print("You Said : ", text)

    translater = Translator()
    out = translater.translate(text, dest="es")
    print("Spanish Translation : ", out.text)

    language = 'es'
    output = gTTS(text=out.text, lang=language, slow=False)
    output.save("output.mp3")

    # Play the converted file
    os.system("start output.mp3")

elif ch == 4:
    r = sr.Recognizer()
    print("Your Speech Will Be Translated Into German")
    with sr.Microphone() as source:

        print('Say Something:')
        audio = r.listen(source)
        print('Done!')

    text = r.recognize_google(audio, language='en-IN')
    print("You Said : ", text)

    translater = Translator()
    out = translater.translate(text, dest="de")
    print("German Translation : ", out.text)

    language = 'de'
    output = gTTS(text=out.text, lang=language, slow=False)
    output.save("output.mp3")

    # Play the converted file
    os.system("start output.mp3")

elif ch == 5:
    r = sr.Recognizer()
    print("Your Speech Will Be Translated Into Russian")

    with sr.Microphone() as source:
        print('Say Something:')
        audio = r.listen(source)
        print('Done!')

    text = r.recognize_google(audio, language='en-IN')
    print("You Said : ", text)

    translater = Translator()
    out = translater.translate(text, dest="ru")
    print("German Translation : ", out.text)

    language = 'ru'
    output = gTTS(text=out.text, lang=language, slow=False)
    output.save("output.mp3")

    # Play the converted file
    os.system("start output.mp3")

elif ch == 6:
    r = sr.Recognizer()
    print("Your Speech Will Be Translated Into French")
    with sr.Microphone() as source:
        print('Say Something:')
        audio = r.listen(source)
        print('Done!')

    text = r.recognize_google(audio, language='en-IN')
    print("You Said : ", text)

    translater = Translator()
    out = translater.translate(text, dest="fr")
    print(out.text)

    language = 'fr'
    output = gTTS(text=out.text, lang=language, slow=False)
    output.save("output.mp3")

    # Play the converted file
    os.system("start output.mp3")

else:
    print("Please Choose Valid Language")
