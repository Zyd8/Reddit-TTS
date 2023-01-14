"""
From PRAW_Credentials.py, there are 3 REQUIREMENTS that are in need of modifying to run
From Scrape_Reddit.py, there are 3 REQUIREMENTS and that are in need of modifying to run 
From Clean_Text, no need to modify anything to run
From Narrate_Text.py, no need to modify anything to run
From Make_Video.py, no need to modify anything to run 
"""

from Scrape_Reddit import find_post
from Clean_Text import clean_post
from Narrate_Text import narrate_post
find_post()
clean_post()
narrate_post()

from Make_Video import merge_export
merge_export()

print("Program executed successfully")