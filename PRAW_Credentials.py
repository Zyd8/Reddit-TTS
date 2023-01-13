"""
We need to input our own created Reddit account to the appropriate variables.

More of this on the documentation (https://praw.readthedocs.io/en/stable/getting_started/quick_start.html).

The purpose of this credentials is for the sole purpose of simply getting access to Reddit's API.

Since we're only reading from the API and not writing to Reddit via API, it is easier to set up. 
If perchance we want to write, read the PRAW docs.

Warning: we must not share this unique credentials to anyone we don't trust, as one's account could get compromised (reason why it's on a seperate file). 
"""

my_client_id = "Enter client ID" # REQUIREMENT
my_client_secret = "Enter client secret" # REQUIREMENT
my_user_agent = "Enter user agent" # REQUIREMENT