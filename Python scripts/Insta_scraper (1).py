#!/usr/bin/python3.6
# use your Instagram username and password on line 13. Run the code and you will get an error and an instruction to set your browser to a page asking if you just logged in.
# Say Yes. and run the script again. It should run this time. If you get a recursion error, refresh this page again by putting your cursor on the URL bar and hitting Enter. Now run the script. Should work.
import instaloader
import  time
import  pandas as pd
import sys
sys.setrecursionlimit(10000)
from datetime import datetime
from itertools import dropwhile, takewhile

L = instaloader.Instaloader()
L.login("instagram userid", "password")
df=pd.DataFrame()

#CODE TO GET DATA FROM AN ACCOUNT

i=0
for post in instaloader.Profile.from_username(L.context, 'natgeo').get_posts():
    df = df.append({'Caption': post.caption, 'Likes': post.likes, 'URL': post.url  }, ignore_index=True)
    df.to_excel("natgeo_New.xlsx",index=False)
    i = i+1
    if i>200:
        break
print("Written to natgeo_new.xlsx file")

