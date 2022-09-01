from langdetect import detect, detect_langs, DetectorFactory

DetectorFactory.seed = 0 # setting seed to ensure reproducability
def conf_ld_detect_language(text):
    try:
        highest_conf = detect_langs(text)[0]
        return highest_conf.lang, highest_conf.prob
    except:   
        return "ident_fail", pd.NA
    return True
