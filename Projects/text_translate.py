from googletrans import Translator

translator = Translator()


translated_text = translator.translate('Imported Bananas.', dest='tr')
print(translated_text.text)
