#!/usr/bin/python
import praw
import pdb
import re
import os

#Create a Reddit instance
reddit = praw.Reddit('bot1')

# Assume replylogfile doesnt exist
if not os.path.isfile("replylogfile.txt"):
		replylogfile = []

# if it does exist, load a list from replylogfile
else:
	#read into a list and remove empty values
	with open("replylogfile.txt", "r") as f:
		replylogfile = f.read()
		replylogfile = replylogfile.split("\n")
		replylogfile = list(filter(None, replylogfile))


# print(reddit.read_only)  # Output = boolean but why care
# what other functions does that praw.Reddit object have (or can be given)?

# Get some posts
for submission in reddit.subreddit('pythonforengineers').top(limit=10):
	#print(submission.title)

	# if it hasnt already been logged
	if submission.id not in replylogfile:
		# case insensitive search of title
		if re.search("NSFW", submission.title, re.IGNORECASE):
			# Reply ot the post as the currntn user
			submission.reply("Your call is Important to us.")
			# Output for the users cos we ike to see stuff happening
			print("And will be returned like a boomerang to ", submission.title)
			# Append an ID to the log file
			replylogfile.append(submission.id)

#Write the list back to the file to keep it safe :)
with open("replylogfile.txt", "w") as f:
				for post_id in replylogfile:
					f.write(post_id + "\n")


# Output should be 10 submission to /r/learnpython

