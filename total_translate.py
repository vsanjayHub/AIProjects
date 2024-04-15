"""This module provides translation capabilities for multiple languages
    using google API.
"""
import re
import os
import html
import requests
from langdetect import detect, LangDetectException

# Initialize the Google Cloud Translation client
def should_translate(text, target_language="en"):
    """
    Convert integer fields .
    :param record: This is dataframe record.
    """
    detected_language = detect(text)
    return detected_language != target_language

def translate_and_detect_language(text, api_key="YOUR_API_KEY_HERE"):
    """
    Convert integer fields .
    :param record: This is dataframe record.
    """
    url = "https://translation.googleapis.com/language/translate/v2"
    try:
        detected_language = detect(text)  # Detect language at the beginning
    except LangDetectException as e:
        return str(e), "error"
    except Exception as e:
        return str(e), "error"
    try:
        if not should_translate(text,"en"):
            # If the text is already in the target language, no translation is needed
            return html.unescape(text), detected_language

        # Constructing the request for translation
        translation_params = {
            'q': text,
            'target': 'en',
            'key': api_key
        }
        # translation_response = requests.post(url, data=translation_params)

        with requests.Session() as session:
            try:
                # Set a reasonable timeout for the request
                translation_response = session.post(url, data=translation_params, timeout=10)
                translation_response.raise_for_status()  # Raises an exception for 4XX/5XX errors

                # Ensure the response is in JSON format
                translation_result = translation_response.json()

            except requests.exceptions.RequestException as e:
                # Handle network-related errors here
                print(f"An error occurred: {e}")
                return None

            except ValueError:
                # Handle cases where json decoding fails
                print("Failed to decode JSON from response")
                return None

        translated_text = translation_result['data']['translations'][0]['translatedText']
        return html.unescape(translated_text), detected_language
    except Exception as e:
        return str(e), "error"
def is_new_key_line(line):
    """
    Determine if a line starts with a new key.
    :param record: This is dataframe record.
    """
    return bool(re.match(r'^\d+ \d+:', line))

def process_and_translate_file(input_file_path, output_file_path, languages_file_path,api_key):
    """
    Convert integer fields .
    :param record: This is dataframe record.
    """
    with open(input_file_path, 'r', encoding='utf-8') as input_file, \
                open(output_file_path, 'w', encoding='utf-8') as output_file, \
                open(languages_file_path, 'w', encoding='utf-8') as languages_file:
        current_key = None
        current_text = []
        for line in input_file:
            if is_new_key_line(line.strip()) :
                if current_key and current_text:
                    full_text = " ".join(current_text).strip()
                    translated_text, detected_language =  \
                                translate_and_detect_language(full_text, api_key=api_key)
                    languages_file.write(f"{current_key}: {detected_language}\n")
                    output_file.write(f"{current_key}: {translated_text}\n")
                parts = line.split(":", 1)
                current_key = parts[0].strip()
                current_text = [parts[1].strip()] if len(parts) > 1 else []
            else:
                current_text.append(line.strip())
        if current_key and current_text:
            full_text = " ".join(current_text).strip()
            translated_text, detected_language = \
            translate_and_detect_language(full_text, api_key=api_key)
            languages_file.write(f"{current_key}: {detected_language}\n")
            output_file.write(f"{current_key}: {translated_text}\n")

# Example usage
INPUT_FILE_PATH = 'comments_output_2.txt'
OUTPUT_FILE_PATH = 'Reviews_tran_8.txt'
API_KEY = os.getenv("GOOGLE_TRANSLATE_API_KEY")
LANGUAGES_FILE_PATH = 'detected_languages_9.txt'
process_and_translate_file(INPUT_FILE_PATH, OUTPUT_FILE_PATH,LANGUAGES_FILE_PATH, API_KEY)
