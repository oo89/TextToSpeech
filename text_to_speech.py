from gtts import gTTS

mytext = input('Enter text to be read: ')
print(mytext[0:10]+'.mp3')

language = input('Type en for English or es or Spanish: ')

myobject = gTTS(text=mytext, lang=language, slow=False)

myobject.save(mytext[0:10]+'.mp3')    