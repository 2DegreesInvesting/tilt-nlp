from textblob import TextBlob

def translate_english(text, from_lang):
    try:
        blob = TextBlob(text)
        return(str(blob.translate(from_lang = from_lang, to = 'en')))
    except:
        return "translation_fail"
    return True
