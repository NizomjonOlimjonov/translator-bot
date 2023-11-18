from googletrans import Translator

translator = Translator()
returnn = translator.translate("hello", dest="uz").text

print(returnn)

while True:
    text = input("NIMA SOZ BOR:     ")
    language = input("qaysi tilni tanlaysan ")
    retur = translator.translate(text, dest=language).text

    print(retur)
