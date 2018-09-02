import os,sys
import sqlite3
import mysql.connector


path = "/home/giovanni/Downloads/dreams/dreams/dreams/"

def addDream(date, dreamNumber, title, mp3, jpg, pdf, link):
        conn = sqlite3.connect('dreams.db')
        conn.execute("INSERT INTO DREAMS (DATE, DREAMNUMBER, TITLE, MP3, JPG, PDF, LINK) VALUES(?, ?, ?, ?, ?, ?, ?)", (date, dreamNumber, title, mp3, jpg, pdf, link));
        conn.commit()
        print (str(dreamNumber) + " " + str(title) + "  added successfully");
        conn.close()    


def getFiles():
    dirs = os.listdir( path )
    dirs.sort()
    return dirs

def readFile(file):
     f = open(path+file, "r")
     lines = f.read()
     return lines

def getDate(dream):
    x = '<time class="entry-time">'
    y = '</time>'
    xIndex = dream.index(x) + len(x)
    yIndex = dream.index(y)
    date = dream[xIndex:yIndex]
    return date

def getDreamNumber(dream):
    dreamTitle = ""
    i = "<title>"
    x = dream.index("<title>") + len(i)
    y = dream.index("</title>")
    dreamTitlesplit = dream[x:y].split(". ")
    return dreamTitlesplit[0]

def getTitle(dream):
    dreamTitle = ""
    i = "<title>"
    x = dream.index("<title>") + len(i)
    y = dream.index("</title>")
    dreamTitlesplit = dream[x:y].split(". ")
    return dreamTitlesplit[1]
#def getWords():

def getMP3(dream):
   mp3 = ""
   splitthedream = dream.split("</a></audio></p>")
   photoextractor = dream.split("http") 
   jpg = ""
   pdffile = []
   mp3file = []
   for x in photoextractor:
      if "jpg" in x and "feature" in x:
          jpg = "http" + x[:x.index("jpg")+3]
      if "pdf" in x:
          pdffile.append(x)
      if "mp3" in x:
          mp3file.append(x)
   mp3filelink = "http" + mp3file[0][:mp3file[0].index('mp3')+3]   
   splitmp3= mp3filelink.split("/")
   for x in splitmp3:
      if "mp3" in x:
        mp3filename=x 
   print(mp3filename)
   if "mp3" in mp3filename:
      mp3 = mp3filename
   return mp3

def getJPG(dream):
   jpg = ""
   jpgname =""
   splitthedream = dream.split("</a></audio></p>")
   photoextractor = dream.split("http") 
   pdffile = []
   mp3file = []
   for x in photoextractor:
      if "jpg" in x and "feature" in x:
          jpg = "http" + x[:x.index("jpg")+3]
   splitjpg = jpg.split("/")
   for x in splitjpg:
      if "jpg" in x:
          return x

def getPDF(dream):
   splitthedream = dream.split("</a></audio></p>")
   photoextractor = dream.split("http") 
   pdffile = []
   for x in photoextractor:
      if "pdf" in x:
          pdffile.append(x)
   for x in pdffile:
      if "pdf" in x:
          string = x[:x.index('pdf"')+3]
          stringsplit = string.split("/")
          for y in stringsplit:
             if ".pdf" in y:
                return y

def getLink(dream):
    string = readFile(dream)
    dreamtitles = string.split('href="')
    links = []
    links = links[6:82]
    for link in dreamtitles:
       if "http://www.formypeople.org/dream" in link and link.startswith("http://www.formypeople.org/dream") and "-" in link:
         index = '/"'
         x = link.index(index)
         if link not in links:
           links.append(link[:x])
    links = links[7:81]
    #for link in links:
    #   print(link)
    #   print()     
    return links  

def extractRecords(files, links):
    count = 0
    for file in files:
        dreamString = readFile(file)
        date = getDate(dreamString)
        dreamNumber = int(getDreamNumber(dreamString))
        title = getTitle(dreamString)
        mp3 = getMP3(dreamString)
        jpg = getJPG(dreamString)
        pdf = getPDF(dreamString)
        link = links[count]
        addDream(date, dreamNumber,title, mp3, jpg, pdf, link)
        count = count + 1

files = getFiles()
file = files[0]
links = getLink(file)
extractRecords(files, links)

