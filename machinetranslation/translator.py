"""
Python translator module that uses AWS Translation API
"""

import boto3
from botocore.exceptions import ParamValidationError


def instance_aws_translator(text: str, source_lang: str, translated_lang: str) -> str:
    translate = boto3.client(
        service_name="translate", region_name="us-east-1", use_ssl=True
    )

    result = translate.translate_text(
        Text=text, SourceLanguageCode=source_lang, TargetLanguageCode=translated_lang
    )
    return result.get("TranslatedText", "")


def english_to_french(english_text: str) -> str:
    """Translate text from english to french"""
    try:
        return instance_aws_translator(english_text, "en", "fr")
    except ParamValidationError:
        return "You didn't enter any text"


def english_to_spanish(english_text: str) -> str:
    """Translate text from english to spanish"""
    try:
        return instance_aws_translator(english_text, "en", "es")
    except ParamValidationError:
        return "You didn't enter any text"


def french_to_english(french_text):
    """Translate text from french to english"""
    try:
        return instance_aws_translator(french_text, "fr", "en")
    except ParamValidationError:
        return "Vous n'avez entré aucun texte"
