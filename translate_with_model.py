from google.cloud import translate
import six

def translate_text_with_model(target, text, model=translate.NMT):
    """Translates text into the target language.

    Make sure your project is whitelisted.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text, target_language=target, model=model)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))


if __name__ == '__main__':
    target = 'mr'
    text = 'We are waiting to watch the movie on Sachin Tendulkar' 
    translate_text_with_model(target,text)
