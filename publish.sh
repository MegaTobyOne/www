#!/bin/bash
# This could simply be an rsync or anftp but it should be one-step

# Prompt for a commit message
read -p "Commit message: " cmsg
# Make an SSH connection to VentraIP
#ssh toby@ventraIP

# Some Git related stuff
#git status
# shorter version
git status -s
#git add .
git commit -a -m "$cmsg"

# Mirror contents of ~/ameliarose.id to IPAddress:/public
# rsync -avz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --progress ~/ameliarose.id 198.168.0.2:/home/ameliaro/public_html

# Good old FTP pehaps
# ftp ?

# Clear any cache or temp files

## Bonus points for read back from location first
