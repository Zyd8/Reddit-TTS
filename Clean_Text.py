"""
Takes the text.txt and cleans it, then writes it to another file (text_clean.txt)
"""
from cleantext import clean

text_folder = "text"
text_file_u = "\\text.txt" 
text_file_c = "\\text_clean.txt" 

def clean_post():
    print("done.")
    print("cleaning...", end="")
    with open(text_folder+text_file_u, "r", encoding="utf-8") as f, open(text_folder+text_file_c, "w", encoding="utf-8") as g:
        clean(f, no_emoji=True) # removes emojis
        for line in f:
            g.write(line)