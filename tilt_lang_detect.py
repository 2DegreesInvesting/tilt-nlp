from langdetect import detect_langs, DetectorFactory
import pandas as pd

DetectorFactory.seed = 0 # setting seed to ensure reproducability
def conf_ld_detect_language(text):
    """Langugae detection wrapper.
    
    Returns detected language (ISO-code) and confidence of detection. In case of 
    failure of detection string "ident_fail" and a pd.NA value for confidence is 
    returned.
    
    Args:
        text (str): The string for which language shall be detected.
    Returns:
        tuple: A tuple holding ISO-code of detected language along with 
        detection confidence.
    """
    try:
        highest_conf = detect_langs(text)[0]
        return highest_conf.lang, highest_conf.prob
    except:   
        return "ident_fail", pd.NA
    return True
