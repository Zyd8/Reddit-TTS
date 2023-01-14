"""
Merges the audio files and screenshots together
"""

from moviepy.editor import *
import os

def lister(list, path):
    for contents in os.listdir(path):
        list.append(contents)

def merge_export():
    print("done")
    print("merging then exporting...", end="")
    final_clip = fin_screensh.set_audio(fin_audio)
    final_clip.write_videofile(str(output_title) + ".mp4", fps=24)
    print("done.")

audio_folder = "audio"
screensh_folder = "screenshot"
output_title = "movie" 

audio_list = []
screensh_list = []
lister(audio_list, audio_folder)
lister(screensh_list, screensh_folder)

if len(audio_list) != len(screensh_list):
    print("Input Error: audio count and screenshot count is not the same\n")
    quit()

aud_cl = []
scr_cl = []
for i in range(1, len(audio_list and screensh_list)+1):
    audio = AudioFileClip(audio_folder+"\\"+str(i)+".mp3")
    aud_cl.append(audio)
    screensh = ImageClip(screensh_folder+"\\"+str(i)+".png")
    screensh = screensh.set_duration(audio.duration)
    scr_cl.append(screensh)

fin_audio = concatenate_audioclips(aud_cl)
fin_screensh = concatenate_videoclips(scr_cl, method='compose')
