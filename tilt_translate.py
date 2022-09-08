from textblob import TextBlob

def translate_english(text, from_lang, to = 'en'):
    """Language translation wrapper.
    
    Returns a string holding provided text translated from original to target
    language. In case of failure of translation string 'translation_fail' is 
    returned.
    
    Args:
        text (str): The string that shall be translated.
        from_lang (str): ISO-code of original language of text.
        to (str): ISO-code of target language of translation. Defaults to 'en'.
    Returns:
        str: Holding translated text.
    """
    try:
        blob = TextBlob(text)
        return(str(blob.translate(from_lang = from_lang, to = to)))
    except:
        return "translation_fail"
    return True
