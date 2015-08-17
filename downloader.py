#!/usr/bin/python


import requests
import os
from bs4 import BeautifulSoup
import wget



headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:38.0) Gecko/20100101 Firefox/38.0\r\n'}

url = raw_input("Enter the Lynda.com Course URL:")
username = raw_input('Enter your username: ')
password = raw_input('Enter your your password: ')
payload = {'username':username,
           'password':password,
           'remember':'true'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text)

video_id_list = []
for links in soup.find_all('a'):
    if not links.get('data-video-id') == None:
        videoid = links.get('data-video-id')
        video_id_list.append(videoid)
        video_id_list.sort()

# Return and Store Course ID #
def get_coursenum(url):
    for links in soup.find_all('a'):
        if not links.get('data-course-id') == None:
            courseid = links.get('data-course-id')
            return courseid

#Add Course ID and Video ID's to to URL and place into dictionary
url_list = []
for vid in video_id_list:
    url_list.append('http://lynda.com/ajax/player?videoId='+vid+'&courseId='+get_coursenum(url)+'&type=video&_=1432595542056"')

#Make Course Folder using Course name Move into that Folder
for name in soup.h1:
    course_folder = name
os.makedirs(course_folder)
os.chdir(course_folder)


session_urls_HD = []
session_urls_SD = []


with requests.Session() as s:
    login = s.post("https://www.lynda.com/login/login.aspx", data=payload)

    for url in url_list:
        search = s.get(url) 
        new_dict = search.text.split('"')
        session_urls_HD.append(new_dict[15])
        session_urls_SD.append(new_dict[25])

    if requests.get(session_urls_HD[0], headers=headers).status_code == 200:
        for url in session_urls_HD:
            wget.download(url)
    else:
       for url in session_urls_SD:
            wget.download(url)


    s.cookies.clear()
    s.get('http://www.lynda.com/ajax/logout.aspx?url=%2fmember.aspx') #llow_redirects=False)
    s.close()
