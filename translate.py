import os
import pyperclip
import time
import requests
from bs4 import BeautifulSoup

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def translate(word):
       urlx = "https://tureng.com/tr/turkce-ingilizce/"
       r = requests.get(str(urlx+word),allow_redirects=False)
       context = r.content
       soup = BeautifulSoup(context, "html.parser")
       for i in soup.find_all("td",{"class":"tr ts"}):
              return str(i.text)
       

copy = pyperclip.paste()
while(true):

       if(copy!=pyperclip.paste()):
              copy = pyperclip.paste()
              notify(copy, translate(copy))
       time.sleep(1)
