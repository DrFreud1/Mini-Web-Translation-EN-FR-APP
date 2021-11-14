'''
Python translator module that uses Watson IBM API
'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

def instance_watson_translator():
    '''Instantiate IBM Translator'''
    apikey = os.environ['apikey']
    url = os.environ['url']
    version='2018-05-01'

    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version = version,
        authenticator = authenticator
    )
    language_translator.set_service_url(url)

    return language_translator

def english_to_french(english_text):
    '''Translate text from english to french'''
    try:
        translation = instance_watson_translator().translate(
            text = english_text,
            model_id = 'en-fr').get_result()

        return translation['translations'][0]['translation']
    except ValueError:
        return "You didn't enter any text"

def french_to_english(french_text):
    '''Translate text from french to english'''
    try:
        translation = instance_watson_translator().translate(
            text = french_text,
            model_id = 'fr-en').get_result()

        return translation['translations'][0]['translation']
    except ValueError:
        return "Vous n'avez entré aucun texte"
