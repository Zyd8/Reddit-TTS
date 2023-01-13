# Reddit-TTS
Imitates those Reddit text-to-speech channels from youtube

It essentially uses the PRAW library to scrape title, selftext, comments, and sub-comments from reddit. Then the data is cleaned and subjected to a text-to-speech engine known as gTTS, which is a library that uses the voice model of which google created. Then it proceeds to be processed by a video/audio/image processing library: moviepy.

Future improvements to make:
* Implement the Selenium library to automatically take screenshots of the targeted data.
* Subject the screenshots to a background remover API to allow flexibility and make room for enticing visuals.
* Implement variables that supports any inserted video/audio transition.

## Link to the rough output with the transitions, background, thumbnail and screenshots, being manually done. But the rest, fully automated.

https://www.youtube.com/watch?v=bFIXDE2WAIU&t=68s