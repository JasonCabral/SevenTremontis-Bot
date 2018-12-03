
# coding: utf-8

# In[48]:

import urllib.request
from bs4 import BeautifulSoup
import datetime
import pandas as pd


# In[43]:

today = datetime.datetime.today().strftime('%m-%d')
holiday = 'Y'


# In[44]:

thanks = 'Sevendust Thank You'
black = 'Sevendust Black'
hanukkah = 'Sevendust Waffle'
solstice = 'Sevendust Seasons'
xmas = 'Sevendust Xmas Day'
yearseve = 'Sevendust The End Is Coming'
newyear = 'Sevendust Failure'
trump = 'Sevendust Denial'
mlkday = 'Sevendust Angels Son'
groundhog = 'Sevendust My Ruin'
valentine = 'Sevendust Bitch'
bigday = 'Tremonti Providence'


# In[45]:

def getTopVid(song):
    searchList = []
    
    textToSearch = song
    
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            searchList.append('https://www.youtube.com' + vid['href'])
            
    while searchList[0].find("https://googleads.g.doubleclick.net") > 0 or     searchList[0].find("https://www.googleadservices.com") > 0:
        searchList.pop(0)
        
    return searchList[0]


# In[94]:

if today == '11-22':
    song = thanks
elif today == '11-23':
    song = black
elif today == '12-03':
    song = hanukkah
elif today == '12-21':
    song = solstice
elif today == '12-25':
    song = xmas
elif today == '12-31':
    song = yearseve
elif today == '01-01':
    song = newyear
elif today == '01-20':
    song = trump
elif today == '01-21':
    song = mlkday
elif today == '02-02':
    song = groundhog
elif today == '02-14':
    song = valentine
elif today == '02-15':
    song = bigday
else:
    inTable = pd.DataFrame.from_csv("SevenTrem2.csv")
    song = inTable[inTable['Played']==0].sample(1)['Song'].item()
    holiday = 'N'


# In[115]:

# Send video via sms-email
# Credit: https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/

import smtplib 
  
# list of email_id to send the mail 

li = ["1234567890@msg.fi.google.com", "1234567890@mymetropcs.com"] 

fromMail = "YOUR_EMAIL@gmail.com"
fromPhone = "1234567890"
appPassword "APP_PASSWORD_FROM_GOOGLE"

for i in range(len(li)): 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromMail, appPassword) 
    message = "From: %s\r\n" % fromMail + "To: %s\r\n" % li[i] + "Subject: %s\r\n" % "" + "\r\n" + getTopVid(song)
    s.sendmail(fromPhone, li[i], message) 
    s.quit() 
    


# In[113]:

if holiday == 'N':
    inTable.loc[inTable['Song'] == song, 'Played']=1
    inTable.to_csv("SevenTrem2.csv")

