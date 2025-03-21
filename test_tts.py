from text_to_speech import text_to_speech

# Example sentiment summary to be converted into speech
summary_text = "टेस्ला की खबरें ज्यादातर सकारात्मक हैं। इसका स्टॉक मूल्य बढ़ सकता है।"

# Generate and save speech file
audio_file = text_to_speech(summary_text)

# Print output file name
if audio_file:
    print(f"Audio saved as: {audio_file}")
