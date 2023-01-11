from Scrape_Reddit import find_post
from Clean_Text import clean_post
from Narrate_Text import narrate_post

find_post()
clean_post()
narrate_post()

from Make_Video import merge_export

merge_export()

print("Program executed successfully")