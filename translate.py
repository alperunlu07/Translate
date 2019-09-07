#!/usr/bin/python3
import os
import pyperclip
import time
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier


def notify(title, means):
       output = ""
       if(os.name == "posix"):
              for i in range(len(means)):
                     output += str(i+1)+": "
                     output += means[i]
                     output += "\t"
                     if(i>5):
                            break
              os.system("""
                     osascript -e 'display notification "{}" with title "{}"'
                     """.format(output, title))
   
       if(os.name == "nt"):
              for i in range(len(means)):
                     output += str(i+1)+": "
                     output += means[i]
                     output += "\n"
                     if(i>10):
                            break
              toaster = ToastNotifier()
              toaster.show_toast(title,output)

def translate(word):
       urlx = "https://tureng.com/tr/turkce-ingilizce/"
       r = requests.get(str(urlx+word),allow_redirects=False)
       context = r.content
       soup = BeautifulSoup(context, "html.parser")
       mean = []              
       for i in soup.find_all("td",{"class":"tr ts"}):
              mean.append(i.text)       
       return mean
#print(translate("book"))
def anlam(means):
       output = ""
       for i in range(len(means)):
              output += str(i+1)+": "
              output += means[i]
              output += "\n"
              if(i>5):
                     break
       return output

copy = pyperclip.paste()
while(True):
       if(copy!=pyperclip.paste()):
              copy = pyperclip.paste()
              notify(copy, translate(copy.lower()))
              
       time.sleep(1)





