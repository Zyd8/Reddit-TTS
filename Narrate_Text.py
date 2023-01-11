"""
Feeds the voice model with the cleaned text and generates mp3 files per title, selftext, and comments to the audio folder
"""

from gtts import gTTS

def narrate_post():
    print("done.")
    print("narrating...", end="")
    name_ctr = 0
    with open(text_folder+text_file, "r", encoding="utf-8") as f:
        content = f.readlines()
        for lines in content:
            tts = gTTS(text=lines)
            name_ctr += 1
            tts.save(audio_folder + str(name_ctr) + ".mp3")
            
text_folder = "text"
text_file = "\\text_clean.txt"
audio_folder = "audio\\"
