from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3"):
    """
    Convert given text into Hindi speech and save as an audio file.

    Args:
    text (str): The text to be converted to speech.
    filename (str): The output file name (default is 'output.mp3').

    Returns:
    str: The filename of the generated audio file.
    """
    try:
        tts = gTTS(text, lang="hi")  # Set language to Hindi
        tts.save(filename)
        return filename
    except Exception as e:
        print("Error generating speech:", e)
        return None
