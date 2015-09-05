# Lynda.com downloader script
I originaly came up with this idea because I wanted an easy way to download 
entire course videos from Lynda.com.

Each course page has an HTML attribute of a course ID and video ID number. 
Combine them with the URL below (logged into your lynda.com account) and you will 
receive a JSON page giving you the URL for each video in the course.

To use the script you will need to install requests and beautiful soup first. You can run the requirements  
script first.

Next find a URL of the course you would like to download and copy the URL
of the course homepage. 

Run the script, enter the course URL, your username and password and you should be all set.
