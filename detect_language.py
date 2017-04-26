#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from google.cloud import translate
def detect_language(text):
    """Detects the text's language."""
    translate_client = translate.Client()

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.detect_language(text)

    print('Text: {}'.format(text))
    print('Confidence: {}'.format(result['confidence']))
    print('Language: {}'.format(result['language']))

if __name__ == '__main__':
    text = u'सेन्सेक्सने प्रथमच ओलांडला 30 हजारांचा टप्पा'.encode('utf-8').strip()
    detect_language(text)
                       
