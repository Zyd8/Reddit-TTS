"""
Finds the submission's title, selftext/description, comments, replies 
then writes it to the text.txt file in the text folder
"""

import praw
from PRAW_Credentials import *

# API credentials
reddit = praw.Reddit(
    client_id = my_client_id,
    client_secret = my_client_secret,
    user_agent = my_user_agent,
)

def call_title(file, submission):
    strpd_sub_title = submission.title.strip()
    strpd_sub_title = strpd_sub_title.replace("\n", "")
    file.write(strpd_sub_title+"\n")  

def call_selftext(file, submission):
    strpd_sub_selftext = submission.selftext.strip()
    strpd_sub_selftext = strpd_sub_selftext.replace("\n", "")  
    file.write(strpd_sub_selftext+"\n")

def call_comments(file, submission):
    main_com_ctr = 0; sub_com_ctr = 0; sub_com_stop = 0;
    # Scrapes the main comments
    for main_com in submission.comments:
        strpd_main_com = main_com.body.strip()
        strpd_main_com = strpd_main_com.replace("\n", "") 
        if (str(strpd_main_com) == "[deleted]"):
            continue 
        file.write(strpd_main_com+"\n")
        main_com_ctr += 1
        if main_com_ctr == main_com_need:
            # If the main comment counter meets what the main comment need, 
            # the sub-comment scraper will run one last time
            for sub_com in main_com.replies:
                strpd_sub_com = sub_com.body.strip()
                strpd_sub_com = strpd_sub_com.replace("\n", "")  
                if (str(strpd_sub_com) == "[deleted]"):
                    continue 
                file.write(strpd_sub_com+"\n")
                sub_com_ctr += 1 
                sub_com_stop += 1
                if sub_com_stop == sub_com_need: # Resets to zero when the sub-comment need is met
                    sub_com_stop = 0
                break
            break
        # Scrapes the sub-comments
        for sub_com in main_com.replies:
            strpd_sub_com = sub_com.body.strip()
            strpd_sub_com = strpd_sub_com.replace("\n", "")  
            if (str(strpd_sub_com) == "[deleted]"):
                continue 
            file.write(strpd_sub_com+"\n")
            sub_com_ctr += 1 
            sub_com_stop += 1
            if sub_com_stop == sub_com_need: # Resets to zero when the sub-comment need is met
                sub_com_stop = 0
                break

def find_post():
    print("verified.")
    print("finding...", end="")
    submission = reddit.submission(url=link_need)
    submission.comment_sort = "top" # OPTIONAL -- How do you want the Reddit thread comments sorted?
    submission.comments.replace_more(limit=2) # OPTIONAL -- How deep do you want your comments go?
    with open(text_folder+text_file, "w", encoding="utf-8") as f:
        call_title(f, submission) # REQUIREMENT
        call_selftext(f, submission) # OPTIONAL -- Omit if needed
        call_comments(f, submission) # REQUIREMENT

text_folder = "text"
text_file = "\\text.txt" # where all the extracted data goes 
link_need = "Enter reddit link you want to extract from" # REQUIREMENT 
main_com_need = "Enter int" # REQUIREMENT -- How many main/top level comments do you want?
sub_com_need = "Enter int" # REQUIREMENT -- How many sub level comments per main/top level comments do you want?



